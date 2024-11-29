from kobart import get_kobart_tokenizer
from transformers import BartForConditionalGeneration
from utils import remove_repeated_sentences

class TextProcessor:
    def __init__(self):
        print("KoBART 모델 로드 중...")
        self.kobart_model = BartForConditionalGeneration.from_pretrained("gogamza/kobart-summarization")
        self.kobart_tokenizer = get_kobart_tokenizer()

    def summarize(self, text):
        """텍스트 요약"""
        try:
            processed_text = text.replace("\n", " ").strip()
            prompt = f"다음을 요약하여 간결한 문장으로 작성하세요: {processed_text}"
            inputs = self.kobart_tokenizer(
                [prompt], max_length=1024, truncation=True, return_tensors="pt"
            )
            summary_ids = self.kobart_model.generate(
                inputs["input_ids"],
                max_length=150,
                min_length=50,
                num_beams=4,
                repetition_penalty=3.0,
                no_repeat_ngram_size=3,
            )
            summary = self.kobart_tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            return remove_repeated_sentences(summary)
        except Exception as e:
            return f"요약 중 오류 발생: {e}"

    def transform_to_official_style(self, text):
        """공식 문체 변환"""
        try:
            processed_text = text.replace("\n", " ").strip()
            prompt = f"다음을 더 정중하고 공식적인 문체로 작성하세요: {processed_text}"
            inputs = self.kobart_tokenizer(
                [prompt], max_length=1024, truncation=True, return_tensors="pt"
            )
            output_ids = self.kobart_model.generate(
                inputs["input_ids"],
                max_length=256,
                num_beams=4,
                repetition_penalty=3.0,
                no_repeat_ngram_size=3,
            )
            transformed = self.kobart_tokenizer.decode(output_ids[0], skip_special_tokens=True)
            return remove_repeated_sentences(transformed)
        except Exception as e:
            return f"공식 문체 변환 중 오류 발생: {e}"
