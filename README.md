# Advanced-Natural-Language-Processing
## Giới thiệu
### 1. NLP là gì?
Quá trình xử lý ngôn ngữ tự nhiên để máy có thể hiểu được
### 2. Taị sao NLP khó?
- Đa dạng
- không trùng lặp kể cả 1 người trong suốt một đời 90% cũng ko lặp lại
### 3. Thi cử
- trình bày lý thuyết seminar để lấy điểm giữa kỳ 50%
- project cuối kỳ: cài đặt chạy chương trình và thi vấn đáp (50%)
- thêm điểm cộng trả lời câu hỏi
## Lecturer
### 1. Ứng dụng NLP

#### 1.1 Linguistics analysis
- từ loại = part-of-speech (hùng biện - 2200 năm trước) # word type
- noun phrase = danh ngữ
- syntax: cú pháp 
- grammar: ngữ pháp/nghệ thuật viết bao gồm từ pháp và câu (cú pháp) - gram = viết (telegram, program, diagram)
- semantic: ngữ nghĩa

vd: I(pronoun) can(modal verb) can(verb) a(vet) can(noun)

=> xử lý các thành phần của câu để tìm ra được ngữ nghĩa của câu nói => có những hành vi/quyết định thích hợp

chasing   ->  chase

1.  morphology  :   hình thái   -> hình thức

2.  grammar     :   ngữ pháp

- lexical   :    ngữ pháp   -> cấu trúc

- syntax    :    cú pháp

3.  sematic     :   ngữ nghĩa   -> nội dung
4.  pramatics   :   ngữ dụng    (hiện tại máy chưa làm được)

#### 1.2 text classification

#### 1.3 text mining

- xác định xu thế chính trị =))

- information extraction vs gaugau

#### 1.4 text sumarization

#### 1.5 text stylometry
- dùng trong điều tra tội phạm

#### 1.6 text similarity

- dùng trong phát hiện đạo văn, đạo văn xuyên ngữ
- độ khó văn bản (khác với khả năng đọc hiểu) tuỳ thuộc vào:
    - độ phổ biến của từ
    - cấu trúc cú pháp
    - tổ chức văn bản
    - write (encode) -> read (decode)

### Reference:
- đọc sách

## 180423

ChatGPT 
- chatbot
- NLP
- LLM (large language model)

Với câu: i am eating rice

0. phonetics: ngữ âm mối quan hệ giữa đơn vị ngôn ngữ với âm thanh

- môn voice processing: xử lý tiếng nói

sound (english) -- phone (latins)

language:
- voice/speech (tự nhiên)
- text (nhân tạo)

=> voice/speech recognition (nhận dạng tiếng nói)
=> text-to-text

vd: microphone - megaphone - mobiphone - telephone

- âm vị phát âm dễ: m, b, p, a

1. morphology: (phân tích hình thái học) - I be eat rice
(hình thái là mối quan hệ ngôn ngữ giữa đơn vị ngôn ngữ với hình thức của nó, vd eat -> eats/eating/ate/eaten, wifes or wives =))))

Chính tả = (ortho)(graphy) = đúng - viết thuộc về morphology

 center theater (American)

 centre theater

 center theatre

 centre theatre (Bristish)

 cái  đúm =)))

2. grammar:
- lexical (từ pháp)
- sentence: syntax (cú pháp) mối quan hệ giữa những đơn vị ngôn ngữ với nhau, vd I=Subject, eat=Verb

3. semantic: content (phân tích nội dung) mối quan hệ giữa hình thức và nội dung

1->3: môn NLP - xử lý ngôn ngữ tự nhiên

4. pragmatic (ngữ dụng) mối quan hệ giữa đơn vị ngôn ngữ với mục đích sử dụng

- wife -- vợ -- bà xã -- phu nhân (formal/informal)

CAT

dóng đoạn - câu - từ: 
paragraph alignment
sentences alignment
word alignment

vì sao hay vì sao =)) có mấy từ?

cuốn sách/quyển sách có mấy từ?

con chim bay trên trời (thế giới quan: con người làm trung tâm)-> the bird fly (in hay on) the sky (thế giới quan: bầu trời như cái lồng bàn)

phương đông: nông nghiệp
rice 
- lúa 
- thóc

phương tây = du mục + công nghiệp
ngựa 
- pony (ngựa con)
- HP horse power (mã lực)

sao
- star
- aster
    - astronomy
    - astronaut
    - asteroid
    - (dis)aster - sao biến mất == thảm hoạ (như disappear)

nhìn - spect
    - (re)spect - khiến người khác phải ngoái nhìn

số nhiều trong tiếng Việt

    - hư từ (function word) (vì nó không mang nghĩa thực) nói về thì/thể/số/dấu (stop word trong xử lý ngôn ngữ) # thực từ (content word) (từ mang nghĩa thực)
        - các
        - những 
    - phương pháp lặp
        - người người 
        - nhà nhà 

số nhiều trong tiếng anh

    - phụ tố
        -tiền tố (prefix)
        - hậu tố (suffix)

9. Parallel text 

sự khác biệt giữa tiếng việt và tiếng anh:

- từ vựng hoá (lexicalization)
- ranh giới từ (word boundary) - tiếng anh: khoảng trắng, tiếng việt: từ và chữ đều là khoảng trắng
    - vd: sinh viên đại học - 2 từ - 4 chữ, hợp tác xã - 1 từ - 3 chữ
    - vd: tốc độ (truyền (thông) tin), trên (bàn (là)) một chai nước
- trật tự từ (word order)
    - cám ơn các bạn đã chú ý, thank you for your listening
    - mẹ đi chợ mới về

- gà qué (tiếng việt cổ)
- chợ búa (tiếng việt cổ)
- chó má (thái)

tiếng hàn tiếng nhật: S + O + V
tiếng việt tiếng anh: S + V + O

10. chatbot: chatgpt (tâm của nó là NLP)

- nếu chỉ xử lý text == single model
- text, img, voice, video == multi-model -- gpt4

- computational models:
    - AI
    - ML (training data - engine)
    - Deep learning 
- computational linguistic: data = corpus
    - corpus = yu liao ku = ngữ liệu khố = collection of spoken/written 
