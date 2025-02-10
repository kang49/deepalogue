<br/>
<p align="center">
  <h2 align="center">Data input manual 📒</h2>

<br>
      <p align="center">
    นี่คือคู่มือวิธีการใช้ Python script ในการ add ข้อมูลเพื่อเตรียมเทรนโมเดล
    <br/>
    <br/>
  </p>
</p>

## Setup 🛠️

1. ติดตั้ง **Python 3.9** ขึ้นไป สามารถดาวน์โหลดที่ **Microsoft Store** ได้เลยจะได้ไม่มีปัญหากับ PATH
2. ติดตั้ง Git เพื่อใช้ในการ **Push** และ **Pull**
3. ทดสอบว่า Python ที่เราติดตั้งถูกต้องหรือไม่ โดยใช้คำสั่ง
    ```bash
    python --version
    ```
    ถ้าเราเห็นเลขเวอร์ชั่นของ Python ที่เราติดตั้งอยู่ แสดงว่า Python ถูกติดตั้งถูกต้อง

4. เปิด Terminal อะไรก็ได้ จะเป็น Command Prompt หรือ PowerShell ได้หมด
5. ใช้คำสั่ง `cd` เข้าไปใน folder ที่ต้องการจะ download เช่น

    ```bash
    cd C:\Users\myname\Downloads
    ```

6. Download source code ทั้งหมดใน Project นี้หรือจะโหลดแค่โฟลเดอร์ dialogue_datasets ก็ได้จาก branch `new_data_update` โดยใช้คำสั่ง
    ```bash
    git clone -b data_new_update <repository-url>
    ```
    ตัวอย่างเช่น
    ```bash
    git clone -b data_new_update https://github.com/kang49/deepalogue.git
    ```
    การ clone จาก branch `data_new_update` จะทำให้คุณได้รับ data ล่าสุดที่ผู้อื่นอัปเดตไว้ แม้ว่าจะยังไม่ได้รับการ merge

7. ใช้คำสั่ง `cd` เข้าไปในโฟลเดอร์ที่เราเก็บโค้ดที่โหลดมา ตัวอย่างเช่น
    ```bash
    cd C:\Users\myname\Downloads\deepalogue-main\dialogue_datasets\wuthering_waves
    ```
8. รันคำสั่ง
    ```bash
    ls
    ```
    
    จะต้องมีไฟล์เป็นอย่างน้อย 2 ไฟล์ที่สำคัญ คือ

        1. data_input.py
        2. data.jsonl


8. รันโค๊ดด้วยคำสั่ง
    ```bash
    python data_input.py
    ```

## ข้อปฎิบัติ 👮

1. เมื่อมีศัพท์เฉพาะของเกม จะต้องใส่ `()` ครอบคำนั้นทุกครั้ง ไม่ว่าจะภาษาอังกฤษหรือไทย หรือใน `context` ก็ตาม เพื่อให้โมเดลจดจำศัพท์เฉพาะได้ดี
2. ศัพท์เฉพาะจะต้องเป็นภาษาอังกฤษ เช่น (Resonator) (Tacet Discord) (Jinzhou) (Terminal)
3. ไม่ต้องใส่ `()` ให้ชื่อตัวละคร แต่จะต้องพิมพ์ชื่อตัวละครเป็นภาษาอังกฤษ
4. ห้ามพิมพ์ภาษาวิบัติ ห้ามเบิ้ลคำ เช่น
    <br>
    "เข้าใจแล้วงับ", "มีอะไรรรร", "กินข้าวยางงคัฟ", "ฮาฟฟู่วว" ❌❌

5. พยายามเว้นวรรคให้เหมาะสม ไม่ต้องถูก syntax เป๊ะๆ แต่ขอไม่ติดกัน
6. ห้ามใช้คำหยาบ
7. ห้ามนำการเมืองในชีวิตจริงมาเกี่ยวข้อง
8. จริงๆทุกคนจะแปลบทไหนก่อนก็ได้ แต่จริงๆอยากให้ค่อยๆช่วยกันแปลตั้งแต่แรก แต่หากใครจะทำบทอื่น ให้เช็กก่อนว่าบทนั้นมีคนทำไปหรือยัง โดยเช็กได้ที่ตารางความคืบหน้าใน **readme** อันนี้แหละ
9. ทุกคนที่กำลังแปล หรือจะแปล ให้ใส่ชื่อ Github ตัวเองไว้ที่ตารางความคืบหน้าทุกครั้ง และคอยอัพเดตสถานะด้วย แล้ว push request ตารางมาได้เลยจะอนุมัติให้
10. ใน 1บทมีผู้แปลได้หลายคน ถ้าตารางเขียนไม่พอก็เขียนไว้ติดๆกันได้เลย

## วิธีการใช้งาน ➕

1. หลังจากที่รันโค้ดแล้ว โปรแกรมจะให้

    ```bash
    Enter A1 (or type /exit to quit):
    ```

    ให้ใส่บทสนทนาหลัก ที่ไม่ใช่ Options คำตอบที่ให้ player เลือก ตัวอย่างเช่น

    ```bash
    Enter A1 (or type /exit to quit): "I'm sorry, I can't do that Rover."
    ```

2. หลังจากนั้นโปรแกรมจะให้

    ```bash
    Enter B1 option (or /next to proceed, /skip to discard):
    ```

    ให้ใส่คำตอบที่เป็น Options ที่ให้ player เลือก (ใส่ได้หลายคำตอบ) และเมื่อตอบหมด หรือไม่มีคำตอบให้พิมพ์ "/next" หรือ "enter" ข้อความว่างไปเลย ตัวอย่างเช่น

    ```bash
    Enter B1 option (or /next to proceed, /skip to discard): It's okay, I understand.
    Enter B1 option (or /next to proceed, /skip to discard): I'm very mad at you Yangyang.
    Enter B1 option (or /next to proceed, /skip to discard): /next
    ```

    หากต้องการยกเลิกกลางคัน ให้พิมพ์ "/skip" แทน

3. หลังจากนั้นโปรแกรมจะให้

    ```bash
    Enter context (or /skip to leave empty):
    ```

    ให้ใส่ข้อความที่ช่วยอธิบายบทสนทนานั้นๆเป็นภาษาไทย ว่าทำไมถึงพูดแบบนี้ หรือทำไมเราถึงตอบแบบนี้ การหาเหตุผลที่ดีจะช่วยให้โมเดลเรียนรู้ได้ดีขึ้น ตัวอย่างเช่น

    ```bash
    Enter context (or /skip to leave empty): คุณมีของที่ต้องรีบนำไปส่งให้ (Resonator) คนอื่นๆให้ไวที่สุด แต่คุณติดภารกิจกระทันหัน คุณจึงขอให้เพื่อนของคุณนำไปส่งแทน แต่เพื่อนคุณกลับปฏิเสธ คุณจะตอบว่าอย่างไรระหว่าง "ไม่เป็นไร ฉันเข้าใจ" หรือ "ฉันโกรธคุณมาก!"

4. หลังจากนั้นโปรแกรมจะให้

    ```bash
    Translated A1:
    Translated B2 (ถ้ามี):
    ```

    ⚠️ ให้ใส่คำแปลของประโยคดังกล่าวเข้าไป แนะนำว่าพยายาม **เลี่ยงภาษาวิบัติ** เช่น
    <br>
    "เข้าใจแล้วงับ", "มีอะไรรรร", "กินข้าวยางงคัฟ", "ฮาฟฟู่วว" ❌❌

5. วนซ้ำแบบนี้ไปเรื่อยๆ แต่ตอนสุดท้าย **ห้ามลืม "/exit"** เด็ดขาด เพราะไม่งั้นมันจะไม่ save

## วิธี Push Request

คุณสามารถส่ง data ที่แปลแล้วด้วยการ push request ตามวิธีนี้

1. เปิด Terminal และใช้คำสั่งต่อไปนี้เพื่อเพิ่มไฟล์ที่แก้ไขแล้ว
    ```bash
    git add <filepath>
    ```
    ตัวอย่างเช่น
    ```bash
    git add data_input.py data.jsonl
    ```
    หรือเพิ่มทั้ง directory
    ```bash
    git add .
    ```

2. ใช้คำสั่งต่อไปนี้เพื่อ commit การเปลี่ยนแปลง โดยใช้ format ชื่อ commit ว่า
    ```bash
    git commit -m "(data_<game name>): จำนวนบรรทัดที่แปล ชื่อบท สถานะ(🚧✅⚠️)"
    ```
    ตัวอย่างเช่น
    ```bash
    git commit -m "(data_wuthering_waves): 50 Cerulean Echoes Adrift in the Winds: Epilogue ✅"
    ```
    **ถ้าชื่อเขียนไม่พอ ให้เขียนในคำอธิบายแทน ส่วนชื่อเอาที่เขียนได้พอไม่ต้องเขียนให้จบ**
    ```bash
    git commit -m "(data_wuthering_waves): 50 Cerulean Echoes ✅"

3. ใช้คำสั่งต่อไปนี้เพื่อ push การเปลี่ยนแปลงไปยัง branch `data_new_update`
    ```bash
    git push origin data_new_update
    ```

4. ไปที่หน้า repository บน GitHub และสร้าง Pull Request จาก branch `data_new_update` ของคุณ

## Tips ✨

ข้อมูลบทเกือบทั้งหมด สามารถหาได้ที่เว็บ [fandom.com - Main Quest](https://wutheringwaves.fandom.com/wiki/Main_Quests), [freedom.com - All dialogue](https://wutheringwaves.fandom.com/wiki/Category:Dialogue)

## ความคืบหน้า 🚧

- ✅ เสร็จ
- 🚧 กำลังดำเนินการ
- ⚠️ หยุดทำโดยยังไม่เสร็จ
- ❌ ถูกลบ, ปฏิเสธอันด้วยมาจากสาเหตุใดๆก็ตาม

| ชื่อเกม | ชื่อบท | ผู้แปล | สถานะ | คาดว่าจะเสร็จ |
|-|-|-|-|-|
|Wuthering Waves| Utterance of Marvels: I | kang49 | 🚧 | 17/02/2025|
|game name| บรรทัดตัวอย่าง ห้ามลบ | username | ✅ | dd-mm-yyyy |