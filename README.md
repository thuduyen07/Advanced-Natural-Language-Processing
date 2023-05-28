# Advanced-Natural-Language-Processing
## Giới thiệu
### 1. NLP là gì?
Quá trình xử lý ngôn ngữ tự nhiên để máy có thể hiểu được
### 2. Taị sao NLP khó?
- Đa dạng
- Nhập nhằng
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

## 250423
- các ngôn ngữ trên thế giới 
- các ngôn ngữ đang ngày một mất đi do kinh tế, đời sống xã hội -> mất đi văn hoá, tri thức, lịch sử
- ngôn ngữ khác từ vựng, từ vựng của tiếng anh nhiều nhưng ngữ pháp không hẳn là logic nhất
- chữ viết là nhân tạo, chỉ có một số ngôn ngữ có chữ viết
- Vietnamese writings:
    - chữ Nôm - Hàn Thuyên (vào thế kỷ thứ 13)
    - chữ Quốc Ngữ - Alexandre de Rhodes
    - đang ghi âm chứ không ghi ý
- Chữ quốc ngữ = latin + dấu thanh(tone mark: sắc - huyền - hỏi - ngã - nặng) + dấu phụ (diacritics: ă, â, ư, ơ, ô)
- latin = hy lạp (greek) (y <-> y greek)
- 
- chữ hàn quốc là khoa học nhất thế giới -> có thể đọc được ngay khi học (chữ được vua Sejong phát âm ~ 1443) -> chữ cái mô tả hình dáng lưỡi khi phát âm


nhắc thầy đưa coursera gửi lớp

chữ viết Do Thái (Hebrew alphabet - dựa trên David star)
-> tiệm kim hoàn = jewelry = tiền của người do thái (jew - người do thái)
- chữ người do thái không có nguyên âm, chỉ có phụ âm (vd: jrslm - jerusalem - jeru (thành phố) và salem (hoà bình))
- có 3 cách phân loại ngôn ngữ:
    1. tất cả ngôn ngữ có cùng một nguồn gốc, được phân thành 5 nhóm (ngữ hệ) theo yếu tố thời gian (diachronic):
        - ngữ hệ > dòng > ngành > nhóm > vùng 
        - ảnh hưởng nhiều bởi địa lý
        1. ấn âu (indo-euro): german -> english (vd kinder(child)-garten(garden))
        2. semitic
        3. thổ (turkish)
        4. sino-tibetan (hán - tạng)
        5. nam phương (austro-asia): Mon-Khmer branch > Viet Muong group > Muong and Vietnamese

    syn(cùng/đồng)-chrony(thời gian)

2. phân theo typology, có 3 nhóm:
    1. flexional languages: phụ thuộc vào ngôi (person) - số - thì (tense) - chủ cách (he) - đối cách (him) - giống (trung/đực/cái), lối(mood)(mệnh lệnh cách, bàn thái cách) - thể (form: nghi vấn, phủ định, khẳng định)
    - trong các ngôn ngữ biến hình, tiếng anh biến hình ít nhất. Vd: we shall -> we will; I/we/you/they go -> he/she goes
    - mức độ biến hình tiếng Pháp cao hơn tiếng Anh
    - mức độ biến hình tiếng Nga cao hơn tiếng Pháp =)) => nó cụ thể hơn do ngữ nghĩa đã nằm trong từ nên thứ tự ko còn quan trọng nữa, khi đó thứ tự dùng để biểu thị sắc thái: formal/informal
    - latin khó nhất =))
    2. Ngôn ngữ chắp dính:
    - tiếng Nhật
    - tiếng Hàn
    3. Isolating (đơn lập): ngôn ngữ không biến hình/rời rạc
    - vd: I see him: tôi thấy anh - anh thấy tôi
    4. đa tầng hợp
3. Trật tự từ (word order typology): SOV => 3! cách 
    1. SOV: 41-51.8%
    2. SVO: 32.4-41.8%

Bài tập về nhà:
- cho biết ngữ hệ - loại hình - trật tự từ - chữ viết của các câu này
- trong ghi âm có 2 loại: ghi âm vị hay ghi âm tiết 
- dùng hệ chữ gì để ghi
- "tiếng anh và tiếng việt khác nhau vì tiếng anh là ngôn ngữ ấn âu còn tiếng việt là ngôn ngữ đơn lập" => so sánh sai cấp 
- tiếng anh - ghi âm - hệ latin để ghi
- tiêng pháp - latin + dấu - 
- madarin - ghi ý và ghi âm - 
- tiếng việt - ghi âm

- cơ hàn = đói rét
- cơ sở = bộ thổ
- cơ khí = bô mộc
- cơ bắp = bộ nhục - muscle - con chuột (theo tiếng latin)
- cơ thị = bộ nữ
3 classification (dựa trên voice):
    - gene(nguồn gốc - history): 5 ngữ hệ 
    - typology (loại hình): 4 loại hình: biến hình - chắp dính - đơn lập (viet - chinese - thái - lào) - đa tầng hợp
    - word order: SOV

language có 2 hình thức thể hiện:
    1. voice (natural)
    2. writing (artifitial)

## 090523
Nhật Bản - 2 syllable - 2 âm tiết
bản - 3 âm vị
hình vị morpheme
âm vị - phoneme
từ vị - lexeme
từ - word - lexicon

CH-K2023
chữ cái (= mẫu tự) = letter 3

mẫu tự (alphabet) 3

ký số (numeric) 4

ký hiệu (symbol) 1

ký tự = chữ cái + ký số + ký hiệu (character) 8

chữ cái + chữ số = alphanumeric

'học sinh' có 2 chữ
'học' có 3 chữ cái
=> chữ # chữ cái

chỉ có tiếng Trung ghi ý, còn lại đều ghi âm
chỉ có tiếng Nhật ghi âm tiết, còn lại đều ghi âm vị

Quốc tế ngữ là ngôn ngữ nhân tạo
- không có nguồn gốc do không phải ngôn ngữ tự nhiên, không mang theo bản sắc của bất kỳ dân tộc nào

Có 5 loại chữ viết:
- ghi âm
    - âm vị (phoneme)
        - nguyên + phụ âm (V+C) (phoneme): gọi là alphabet - latin, greek, cyrillic (nga)
        - alphabet mà không có nguyên âm (abjad): hebrew, arabic (ví dụ chữ do thái)
        - aphabet với nguyên âm như một đặc trưng (abugida): hangeul, thai, lao
    - âm tiết (syllabary): tiếng nhật (hira, kata)
- ghi ý: hán 

> ## Phân biệt tiếng Việt và tiếng Anh đương đại
- khác nhau lớn nhất: tiếng việt(là ngôn ngữ đơn lập) và các ngôn ngữ đơn có đơn vị **chữ** (morpho-syllabel ~ hình tiết) trong khi tiếng anh không có đơn vị này
- tiếng anh có 6 cấp độ ngôn ngữ, tiếng việt có 7 cấp độ ngôn ngữ
3 cấp đặc điểm:
- ngôn ngữ tự nhiên (tất cả các ngôn ngữ nói chung): ambiguous (nhập nhằng)
    - là hiện tượng xã hội, ko phải hiện tượng tự nhiên, không di truyền
    - hình thức giap tiếp quan trọng để giao tiếp giữa con người 
    - **hệ thống** (có mối quan hệ với nhau) tín hiệu đặc biệt gồm: biểu hiện (hình thức: sound/image) và được biểu hiện (nội dung)
        - phoneme: smallest unit of voice (âm vị)
        - morpheme: (có nghĩa) smallest unit carrying the meaning (hình vị) gồm 2 loại free (tự do) và bound (bị ràng buộc), ví dụ:
            - học sinh có 2 hình vị 
            - bất (không) trắc (đo lường) (trắc nghiệm, sinh trắc, nhân trắc học...)
            - lãng (sống nay đây mai đó) tử (người con trai) - đồng âm dẫn đến: chớt lãng nhách =))
            - giai (đẹp/hay) nhân/điệu/thoại
            - giai (bậc thềm) cấp/đoạn
            - giai (cùng nhau) lão 
            - tối (nhất) ưu (tốt) => không dùng tối ưu hơn, tối ưu nhất
            - hầu hết hán việt là bound morpheme
        - word: (dùng độc lập được) free morpheme, ví dụ "tôi là giáo viên"/"I am teacher"
            - 3 word
            - 4 morpheme (teach|er 2 morpheme) - er, giáo và viên là các hình vị không độc lập (bound morpheme)

            > học sinh
                - 1 từ
                - 2 chữ
                - 2 âm tiết
                - 2 hình vị
            
        - phrase: many word
        - sentence
        - text
    - Ngôn ngữ là sự quy ước của cộng đồng, nên nhiều cái sai nhưng dùng nhiều thành đúng, ví dụ:
        - chúng cư
        - thống kế
    
- loại hình (ngôn ngữ đang xét):
- ngôn ngữ (ngôn đang xét, nói riêng)

literal: chữ nghĩa

letter: chữ cái

script: ký/viết

grapheme: tự vị

syllable: âm tiết

writing chữ viết

monosyllable đơn tiết

BTVN

Tất cả các chữ tiếng việt có tương đương với hình vị không (đều có nghĩa)? Cho ví dụ? Phân loại

vd: cà phê - vì vay mượn từ tiếng pháp - nên không có nghĩa

TH1: từ vay mượn (cà phê, ban công)

TH2: từ láy (long lanh, lấp lánh)

TH3: từ cổ - mờ nghĩa/mất nghĩa
 - gà qué, chó má, chợ búa, 
 - đểu cáng - đểu(phu khiêng đồ) cáng(phu khiêng người), 
 - bù nhìn, bồ câu, mồ hôi, 
 - cốt(xương) cách(da), viên(tròn) mãn(đầy), hàn(lạnh) huyên(nóng), hàn thử biểu (nhiệt kế), ẩm(uống) thực(ăn)
 - quản = ống: khí quản, thực quản, 
 đáo(đến) để(đáy), hô(thở) hấp(hít), 
 đăm(trái) chiêu(phải)=> cân nhắc kỹ lưỡng, vd: chân đăm đá chân chiêu
 - *: aster(star)|isk(small)
 - dis(disappear)|aster(star) 
 - dict(nói)|ion(sự)|ary() => predict(nói trước/tiên đoán), contra(ngược lại)|dict(nói), dictation(đọc chính tả), dictator(độc tài)
 - intro(nhập/vào)|duct(dẫn|ion(sự)
 - e|duc(dẫn dắt)|ation
 - ped(trẻ em)|agogy(người dạy dỗ)
 - philo(yêu)|sophy(sự thông thái)
 - sui(tự)|cide(tử), pesti(sâu bọ)|cide(chớt), geno(thế hệ)|cide(chớt) = diệt chủng
TH4: 

ch - v : không ổn định - phoneme

## 160523

tôi(từ đơn) là(từ đơn) giáo(hình vị) viên

> Phân biệt từ đơn vs. hình vị:
Chữ ~ hình vị vì các từ vay mượn là chữ nhưng không là hình vị(ví dụ: cà phê)

Hình vị:
- Tự do = từ đơn 
- Ràng buộc: hầu hết Hán Việt (giáo viên, đại học, học sinh)

Tôi là một giáo viên - 4 từ - 5 chữ

I am a teacher - 4 từ

=> trong tiếng Việt, khoảng trắng vừa phân biệt từ, vừa phân biệt hình vị => nhập nhằng

Phương pháp giải quyết: 
1. LRMM - left right max match(heuristic): duyệt và lấy cụm các chữ lớn nhất xuất hiện trong từ điển (3/4 chữ)
- nhưng sai trong 1 số trường hợp như: "trên |bàn là| một chai nước", "một ông |quan tài| giỏi", "tốc độ |truyền thông| tin"

> hệ thống của ngôn ngữ tự nhiên, các bình diện gồm
1. ngữ âm: âm vị < âm tiết
2. hình thái: hình vị
3. ngữ pháp: từ pháp + cú pháp
4. ngữ nghĩa
5. 

> Tiếng Việt
- ngôn ngữ đơn lập
- không biến hình (của loại hình đơn lập)
- phương thức ngữ pháp (grammatical methods): là trật tự từ(word order) và hư từ(function word) nhằm thể hiện ý nghĩa ngữ pháp
    - ý nghĩa ngữ pháp (hư từ - function word) bao gồm số/thì/thể(s/es, những, đang)>< ý nghĩa từ vựng(thực từ - content word)(book, cuốn, sách, làm)
    - BOW - bag of words không chú trọng trật tự từ
    - BERT -  có chú trọng trật tự từ, thích hợp với ngôn ngữ đơn 
- tồn tại đơn vị đặc biệt morpho-syllable (hình tiết): tiếng (phát âm) = âm tiết(phát âm - mang tính hàn lâm hơn) = chữ (viết) (của loại hình đơn lập)
- biên giới từ (word boudary) nhập nhằng. Ví dụ: học sinh học sinh học
- word segmentation là tác vụ tiên quyết để làm các tác vụ khác như spelling checker, POS tagger...
    - liên từ "và": khác "tù và", khác động từ "và"
- có các từ chỉ loại (special classifier) đi với các danh từ: *cái* bàn, *cuốn* sách, *bức* thư, *con* chó, *con* sông, *vì* sao, *ngôi* sao... -- đặc điểm của ngôn ngữ đơn lập hay **không**? thái viet han nhat lao
- thanh điệu -- đặc điểm của cấp nào? của riêng tiếng việt hay đơn lập
- âm vị siêu đoạn tính (suppra-segmental phoneme)
    - "toán" có 5 âm vị(vì nó tính luôn cả thanh điệu)
    - thanh điệu khiến tần số âm tiết khác nhau toàn bộ giữa "toán" và "toàn"
- từ láy
- nói lái(spoonerism) có hiện tượng này vì tiếng việt kết cấu lỏng lẻo 3 phần gồm phụ âm đầu, vần và thanh điệu -- còn tiếng nào có tính chất này không? 

> tiếng anh
- ngôn ngữ biến cách theo thì/thể/số
- ý nghĩa ngữ pháp nằm trong từ
- phương thức ngữ pháp: hậu tố (suffix)
- hình thành từ bằng cách thêm tiền - hậu tố. 

ví dụ: anti(chống)|com(cùng nhau)|put|er|iza|tion|al - liên quan đến việc chống lại điện toán hoá

anti|dis(tách)|establishment(nhà thờ can thiệp vào chính quyền/thành lập)|ar(chỉ tính từ)|ian|ism(chủ nghĩa): chủ nghĩa của những người chống lại việc tách rời nhà thờ ra khỏi chính quyền

tiếng việt vs. tiếng anh khác nhau:
- loại hình
- văn hoá 
    - thế giới quan: (in the sky/trên trời)
    - (xưng khiêm - tôi, hô tôn - ngài) 
    - địa lý (vào nam ra bắc) - lịch sử 
    - nông nghiệp vs. du mục
- tiêng việt thiên về động hoá (verbalization) 
- tiếng anh thiên về danh hoá (normalization)

> đề tài: 6 nhóm (chọn cái tô màu vàng) - làm cá nhân
nhóm 1: ứng dụng - prompt engineering

nhóm 2: tìm hiểu công cụ - phân biệt đâu là máy/người viết -- có thể code demo phần detect

nhóm 3: code - xây dựng ứng dụng (có thể dùng API)

nhóm 4: xây dựng một ứng dụng tương tự chatgpt

nhóm 5: xây dựng api

nhóm 6: đề tài hán nôm

## 230523
## Section 2: Formal languages (ngôn ngữ hình thức)

> trong ngôn ngữ hình thức, alphabet là tập hữu hạn gồm các ký hiệu, ký hiệu là $\Sigma$ 

> từ(word) + cụm cố định(fixed phrase) = từ điển (dictionary) = symbols

cụm cố định gồm:
1. phrasal verb
2. idiom - thành ngữ 
3. proverb - tục ngữ (kinh nghiệm dân gian)
4. sayings - quán ngữ

note: thuỷ, giáo, viên,... không thuộc $\Sigma$ tiếng việt vì nó không là từ

a new book -- cụm tự do

grade = bước (lớp)

gradually = dần dần

graduate = bước ra khỏi

upgrade = nâng cấp

va(trống)|cancy = chỗ trống

vacuum = chân không

evacuate = di tản

va(trống)|cation = nghỉ dưỡng

> string (câu/sequence) là một dãy hữu hạn các symbols (gồm từ và cụm từ cố định)

|Formal language  | natural language |
|---|---|
|symbols | word/fixed phrase |
|$\Sigma$ alphabet | dictionary |
| string | sentence |

câu lệnh
- hệ điều hành command
- ngôn ngữ cấp cao statement
- assembly instruction 

ngôn ngữ máy (ML)
- $\Sigma$(ML) = {0, 1}
- string: eg. 101011

> Lực lượng (length) của string là số symbols của nó

$\Sigma^n$ là tập tất cả các phần tử có chiều dài là n

$]Sigma^*$ = $\Sigma^0$ hợp $\Sigma^1$ hợp ... 

$]Sigma^+$ = $\Sigma^1$ hợp $\Sigma^2$ hợp ... 

Một chuỗi trên $\Sigma$: x.a (concate), trong đó w là string (w $\in \Sigma^*$), a là symbol (a $\in \Sigma$)

Lực lượng chuỗi nối: |x.y| = |x| + |y|

BTVN: cho một chuỗi bất kỳ, kiểm tra chuỗi đó có là chuỗi trên $\Sigma$. Viết vòng lặp, kiểm tra từng symbol có thuộc $\Sigma$ không, nếu ko mình break :'>

> Ngôn ngữ có 2 thứ tự (language order): 
- chuẩn hoá (normalize)
- dictionary (alphabet)

$\Sigma^2$ = {giáo viên nghiên cứu}

> Ngôn ngữ là gì?
- là phương tiện giao tiếp (theo nhân văn)
- là một hệ thống tín hiệu (theo kỹ thuật)
- là một subset của $\Sigma^*$

> Làm sao để xác định subset?

Ngôn ngữ hình thức chỉ giải quyết được grammar và nó có algo, trong khi để giải quyết bình diện semantic ta chỉ có thể dùng heuristic 

| | Grammar | Semantic |
|-|---|---|
|tôi ăn bài|v|x|
|tôi ăn cơm|v|v|
|tôi ăn rice| $\notin \Sigma$ | khỏi xét|
|tôi cơm ăn|x|x|

grammar dùng để kiểm tra câu nào đúng câu nào không, vì số lượng câu hợp lệ là vô vùng lớn

> Có 4 loại văn phạm (grammar) (theo Chomsky)
0. unrestricted grammars (UG) (văn phạm không hạn chế - không có giải thuật)
1. context-sensitive (CSG) (cảm ngữ cảnh, ie. phụ thuộc vào ngữ cảnh - không có giải thuật) 
2. context-free (CFG) (Văn phạm phi ngữ cảnh) - đang học 
3. regular (RG) (Văn phạm chính quy)

$G=(\N,\Sigma, P, S)$

trong đó:

$\N$ = non-terminal ~ phạm trù ngữ pháp gồm

$\Sigma$ = terminal

P = production rule

S = start


> production rule (luật sinh) gồm:

S -> NP VP

NP -> pro | n

VP -> v_i (nội động từ không cần object) | v_t NP_i

Luật:
0. Văn phạm không hạn chế (UG)
1. CSG

NP = noun phrase

VP = verb phrase

> Derivation (dẫn xuất) ký hiệu là =>

$L(G)={w|w \in \Sigma^*) giao (S=>^* w)}$

S => ... => pronoun v_t n => I eat rice

phân thành từ loại => tra từ điển 

trên một cây, tồn tại ít nhất 1 đường đến đích => câu đúng
không tồn tại đường đến đích => câu sai
tồn tại nhiều đường => câu nhập nhằng

1. S => NP VP => pro VP => (left most)
2. (right most)
3. (inconsistency) không được làm

BTVN:
1. I sleep
2. I sleep rice
3. you(pro) eat
4. you sleep I(pro)
5. you sleep rice







