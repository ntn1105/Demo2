from googletrans import Translator
import time

def translate_to_vietnamese_or_english(text):
    translator = Translator()

    # Xác định mã ngôn ngữ nguồn
    src_lang = translator.detect(text).lang

    # Xác định mã ngôn ngữ đích
    dest_lang = 'vi' if src_lang == 'en' else 'en'

    # Dịch văn bản
    translated_text = translator.translate(text, src=src_lang, dest=dest_lang)

    return translated_text.text

def main():
    print("Dịch tiếng Anh sang tiếng Việt và ngược lại.")
    
    while True:
        text = input("Nhập văn bản cần dịch (Nhập 'exit' để thoát): ")
        
        if text.lower() == 'exit':
            break

        translated_text = translate_to_vietnamese_or_english(text)

        print(f"Văn bản dịch: {translated_text}")

        # Đợi một lát trước khi tiếp tục để tránh chặn
        time.sleep(1)

if __name__ == "__main__":
    main()
