from PyQt5.QtWidgets import QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QLabel
from text_processor import TextProcessor

class TextProcessorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # 텍스트 처리기 초기화
        self.text_processor = TextProcessor()

        # GUI 구성
        self.setWindowTitle("텍스트 처리 도구")
        self.setGeometry(200, 200, 800, 600)

        # 입력 텍스트
        self.input_text = QTextEdit(self)
        self.input_text.setPlaceholderText("텍스트를 입력하세요...")

        # 출력 텍스트
        self.output_text = QTextEdit(self)
        self.output_text.setReadOnly(True)

        # 요약 버튼
        self.summarize_button = QPushButton("요약")
        self.summarize_button.clicked.connect(self.summarize_text)

        # 공식 문체 변환 버튼
        self.transform_button = QPushButton("공식 문체 변환")
        self.transform_button.clicked.connect(self.transform_text)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(QLabel("입력 텍스트"))
        layout.addWidget(self.input_text)
        layout.addWidget(self.summarize_button)
        layout.addWidget(self.transform_button)
        layout.addWidget(QLabel("출력 텍스트"))
        layout.addWidget(self.output_text)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def summarize_text(self):
        """요약 버튼 클릭 핸들러"""
        text = self.input_text.toPlainText().strip()
        if not text:
            self.output_text.setPlainText("요약할 텍스트를 입력하세요!")
            return

        summary = self.text_processor.summarize(text)
        self.output_text.setPlainText(summary)

    def transform_text(self):
        """공식 문체 변환 버튼 클릭 핸들러"""
        text = self.input_text.toPlainText().strip()
        if not text:
            self.output_text.setPlainText("공식 문체로 변환할 텍스트를 입력하세요!")
            return

        transformed = self.text_processor.transform_to_official_style(text)
        self.output_text.setPlainText(transformed)
