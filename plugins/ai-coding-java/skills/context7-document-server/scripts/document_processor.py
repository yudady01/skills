from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
import os
import hashlib
from pathlib import Path
import markdown
import PyPDF2
from bs4 import BeautifulSoup
import re

class DocumentProcessor(ABC):
    @abstractmethod
    async def process(self, file_path: str) -> Dict[str, Any]:
        """处理文档并返回结构化数据"""
        pass

    @abstractmethod
    def supported_extensions(self) -> List[str]:
        """返回支持的文件扩展名"""
        pass

class MarkdownProcessor(DocumentProcessor):
    def supported_extensions(self) -> List[str]:
        return ['.md', '.markdown']

    async def process(self, file_path: str) -> Dict[str, Any]:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 提取元数据
        metadata = self._extract_metadata(content)

        # 分块处理
        chunks = self._chunk_content(content)

        # 生成文档ID
        doc_id = self._generate_doc_id(file_path, content)

        return {
            'doc_id': doc_id,
            'title': metadata.get('title', Path(file_path).stem),
            'content': content,
            'chunks': chunks,
            'metadata': metadata,
            'file_path': file_path,
            'format': 'markdown'
        }

    def _extract_metadata(self, content: str) -> Dict[str, Any]:
        """提取 Markdown 文件的元数据"""
        metadata = {}
        lines = content.split('\n')

        # 提取标题
        for line in lines:
            if line.strip().startswith('# '):
                metadata['title'] = line.strip()[2:]
                break

        # 提取 YAML frontmatter
        if content.startswith('---'):
            frontmatter_end = content.find('---', 3)
            if frontmatter_end != -1:
                frontmatter = content[3:frontmatter_end]
                try:
                    import yaml
                    metadata.update(yaml.safe_load(frontmatter))
                except:
                    pass

        return metadata

    def _chunk_content(self, content: str, chunk_size: int = 512) -> List[str]:
        """将文档内容分块"""
        # 移除 Markdown 语法但保留结构
        html = markdown.markdown(content)
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text()

        # 清理空白字符
        text = re.sub(r'\s+', ' ', text).strip()

        # 按句子和段落分块
        sentences = re.split(r'[.!?。！？]+', text)
        chunks = []
        current_chunk = ""

        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue

            if len(current_chunk) + len(sentence) < chunk_size:
                current_chunk += sentence + ". "
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = sentence + ". "

        if current_chunk:
            chunks.append(current_chunk.strip())

        # 如果分块太少，按段落分块
        if len(chunks) < 2:
            paragraphs = content.split('\n\n')
            chunks = []
            current_chunk = ""

            for paragraph in paragraphs:
                paragraph = paragraph.strip()
                if not paragraph:
                    continue

                if len(current_chunk) + len(paragraph) < chunk_size:
                    current_chunk += paragraph + "\n\n"
                else:
                    if current_chunk:
                        chunks.append(current_chunk.strip())
                    current_chunk = paragraph + "\n\n"

            if current_chunk:
                chunks.append(current_chunk.strip())

        return chunks if chunks else [content]

    def _generate_doc_id(self, file_path: str, content: str) -> str:
        """生成唯一的文档ID"""
        content_hash = hashlib.md5((file_path + content).encode()).hexdigest()[:12]
        return f"doc_{content_hash}"

class PDFProcessor(DocumentProcessor):
    def supported_extensions(self) -> List[str]:
        return ['.pdf']

    async def process(self, file_path: str) -> Dict[str, Any]:
        content = ""
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                content += page.extract_text() + "\n"

        chunks = self._chunk_content(content)
        doc_id = self._generate_doc_id(file_path, content)

        return {
            'doc_id': doc_id,
            'title': Path(file_path).stem,
            'content': content,
            'chunks': chunks,
            'metadata': {},
            'file_path': file_path,
            'format': 'pdf'
        }

    def _chunk_content(self, content: str, chunk_size: int = 512) -> List[str]:
        """PDF 文档分块处理"""
        # 清理文本
        content = re.sub(r'\s+', ' ', content).strip()

        # 按段落分块
        paragraphs = content.split('\n')
        chunks = []
        current_chunk = ""

        for paragraph in paragraphs:
            paragraph = paragraph.strip()
            if not paragraph:
                continue

            if len(current_chunk) + len(paragraph) < chunk_size:
                current_chunk += paragraph + " "
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = paragraph + " "

        if current_chunk:
            chunks.append(current_chunk.strip())

        return chunks if chunks else [content]

    def _generate_doc_id(self, file_path: str, content: str) -> str:
        """生成唯一的文档ID"""
        content_hash = hashlib.md5((file_path + content).encode()).hexdigest()[:12]
        return f"doc_{content_hash}"

class HTMLProcessor(DocumentProcessor):
    def supported_extensions(self) -> List[str]:
        return ['.html', '.htm']

    async def process(self, file_path: str) -> Dict[str, Any]:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')

        # 提取标题
        title = ""
        title_tag = soup.find('title')
        if title_tag:
            title = title_tag.get_text().strip()

        # 移除脚本和样式
        for script in soup(["script", "style"]):
            script.decompose()

        # 提取正文
        text_content = soup.get_text()

        # 清理空白字符
        text_content = re.sub(r'\s+', ' ', text_content).strip()

        chunks = self._chunk_content(text_content)
        doc_id = self._generate_doc_id(file_path, text_content)

        return {
            'doc_id': doc_id,
            'title': title or Path(file_path).stem,
            'content': text_content,
            'chunks': chunks,
            'metadata': self._extract_metadata(soup),
            'file_path': file_path,
            'format': 'html'
        }

    def _extract_metadata(self, soup: BeautifulSoup) -> Dict[str, Any]:
        """提取 HTML 文件的元数据"""
        metadata = {}

        # 提取 meta 标签
        for meta in soup.find_all('meta'):
            name = meta.get('name') or meta.get('property')
            content = meta.get('content')
            if name and content:
                metadata[name] = content

        return metadata

    def _chunk_content(self, content: str, chunk_size: int = 512) -> List[str]:
        """HTML 内容分块处理"""
        # 按句子分块
        sentences = re.split(r'[.!?。！？]+', content)
        chunks = []
        current_chunk = ""

        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue

            if len(current_chunk) + len(sentence) < chunk_size:
                current_chunk += sentence + ". "
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = sentence + ". "

        if current_chunk:
            chunks.append(current_chunk.strip())

        return chunks if chunks else [content]

    def _generate_doc_id(self, file_path: str, content: str) -> str:
        """生成唯一的文档ID"""
        content_hash = hashlib.md5((file_path + content).encode()).hexdigest()[:12]
        return f"doc_{content_hash}"

class TextProcessor(DocumentProcessor):
    def supported_extensions(self) -> List[str]:
        return ['.txt', '.text']

    async def process(self, file_path: str) -> Dict[str, Any]:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        chunks = self._chunk_content(content)
        doc_id = self._generate_doc_id(file_path, content)

        return {
            'doc_id': doc_id,
            'title': Path(file_path).stem,
            'content': content,
            'chunks': chunks,
            'metadata': {},
            'file_path': file_path,
            'format': 'text'
        }

    def _chunk_content(self, content: str, chunk_size: int = 512) -> List[str]:
        """文本文件分块处理"""
        # 清理空白字符
        content = re.sub(r'\s+', ' ', content).strip()

        # 按段落分块
        paragraphs = content.split('\n')
        chunks = []
        current_chunk = ""

        for paragraph in paragraphs:
            paragraph = paragraph.strip()
            if not paragraph:
                continue

            if len(current_chunk) + len(paragraph) < chunk_size:
                current_chunk += paragraph + " "
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = paragraph + " "

        if current_chunk:
            chunks.append(current_chunk.strip())

        return chunks if chunks else [content]

    def _generate_doc_id(self, file_path: str, content: str) -> str:
        """生成唯一的文档ID"""
        content_hash = hashlib.md5((file_path + content).encode()).hexdigest()[:12]
        return f"doc_{content_hash}"

class DocumentProcessorFactory:
    def __init__(self):
        self.processors = {
            'markdown': MarkdownProcessor(),
            'pdf': PDFProcessor(),
            'html': HTMLProcessor(),
            'text': TextProcessor()
        }

    def get_processor(self, file_path: str) -> Optional[DocumentProcessor]:
        """根据文件扩展名获取对应的处理器"""
        ext = Path(file_path).suffix.lower()

        for processor in self.processors.values():
            if ext in processor.supported_extensions():
                return processor

        return None

    async def process_document(self, file_path: str) -> Optional[Dict[str, Any]]:
        """处理文档"""
        processor = self.get_processor(file_path)
        if processor:
            return await processor.process(file_path)
        return None