<br/>
<p align="center">
  <h3 align="center">DeepAlogue</h3>

  <p align="center">
    แปล Dialogue เกมเป็นภาษาไทยด้วย LLM
    <br/>
    <br/>
    <a href="https://github.com/kang49/deepalogue/issues">Report Issues</a>
  </p>
</p>

<p align="center">
  <a href="https://github.com/kang49/deepalogue">
    <img src="https://img.shields.io/github/repo-size/kang49/deepalogue.svg?style=for-the-badge&logo=appveyor" alt="Size">
  </a>
  <a href="https://github.com/kang49/deepalogue/issues">
    <img src="https://img.shields.io/github/issues/kang49/deepalogue.svg?color=orange&style=for-the-badge&logo=appveyor" alt="Issues">
  </a>
  <a href="https://github.com/kang49/deepalogue/pulls">
    <img src="https://img.shields.io/github/issues-pr-closed/kang49/deepalogue.svg?style=for-the-badge&logo=appveyor" alt="PullRequestsClosed">
  <a href="https://github.com/kang49/deepalogue/forks">
    <img src="https://img.shields.io/github/forks/kang49/deepalogue?style=for-the-badge" alt="Forks">
  </a>
  <a href="https://github.com/kang49/deepalogue/stargazers">
    <img src="https://img.shields.io/github/stars/kang49/deepalogue?color=gold&style=for-the-badge" alt="Stars">
  </a>
  <a href="https://github.com/kang49/deepalogue/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/kang49/deepalogue?style=for-the-badge" alt="License">
  </a>
   <a href="https://github.com/kang49/deepalogue/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/kang49/deepalogue?color=black&style=for-the-badge" alt="Contributers">
  </a>
  <a href="https://github.com/kang49/deepalogue/graphs/releases">
    <img src="https://img.shields.io/github/downloads/kang49/deepalogue/total.svg?style=for-the-badge&logo=appveyor" alt="Contributers">
  </a>
</p>

## About The Project 😃

บางครั้งเรามีเกมที่เราชอบมากๆ แต่น่าเสียดายที่เกมนั้นไม่มีแปลไทย (โคตร Sad) จะนั่งแปลเองก็เหนื่อยมากๆ ยิ่งเป็นเกมเนื้อเรื่องยาวๆ 6-8ชม. นี่ไม่ไหวเลย เราก็เลยคิดเอา LLM มาช่วยแปล ตอนแรกก็ว่าจะเก็บไว้ใช้คนเดียว เพราะ CodeBase แย่จัดๆสร้างมาแบบรีบๆแปลได้ก็พอ555 แต่ก็คิดว่าน่าจะมีคนที่อยากได้อะไรแบบนี้เหมือนกัน ก็เอาลง Github ไปใช้กันฟรีๆเลยละกันนะ ใครอยากมาช่วย Contribute ก็เอาเลย

## Help Us Translate for Model Learning 💭

We plan to enhance the model specifically for a game. By training it with game-specific dialogues data, the translations will be more natural and accurate.

[Click Here](https://github.com/kang49/deepalogue/blob/main/dialogue_datasets/manual.md) to see more detail

## Translation Dataset Progress 🚧 - [Click Here](https://github.com/kang49/deepalogue/blob/main/dialogue_datasets/manual.md#%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%84%E0%B8%B7%E0%B8%9A%E0%B8%AB%E0%B8%99%E0%B9%89%E0%B8%B2-)




<h2>Project Screenshots 🏞️</h2>
<div style="display: flex;">
<img src="https://i.imgur.com/2RZtNUC.png" alt="project-screenshot" width="500">

<img src="https://i.imgur.com/5BzBagQ.png" alt="project-screenshot" width="500">
</div>
<div style="display: flex;">
<img src="https://i.imgur.com/Txs1PE3.png" alt="project-screenshot" width="500">

<img src="https://i.imgur.com/qTM891J.png" alt="project-screenshot" width="500">
</div>

## Installations 🛠️

1. Download exe file from [Release](https://github.com/kang49/deepalogue/releases)
2. Should create folder for it. and put exe file in that folder. I don't build setup file yet.
3. Download Ollama from [Ollama](https://ollama.com/)
4. Open PowerShell or CMD and run this command to download LLM model
   
    ``` sh
    ollama pull gemma2
    ```

5. Run exe file and enjoy it.

## Usage 📚
##### WARNING ⚠️: This program use a lot of memory and GPU power. If you have a low spec computer, you should use it carefully.

1. First time, you open the program. You will see the 3 buttons.
    - Start - Start the program to listen f12 hotkey.
    - Overlay - Show the start button overlay if hotkey not work. You can     move it by drag and drop. 
    - Stop - Stop the program.
    - Reset Position - Clear the overlay position
2. If you first time use, it will open 2 fullscreen overlay. One is a A1 that for message from people in game. Another one is B1 that for message options you reply.

    ***Note: if after you crop area of screen, it not responsding, Don't worry it's normal and happen just first time.***

3. Everytime you use first after open the program, it use a few seconds to load the model. After that, it will be faster.

## Thank you EasyOCR for detect messages 📷

This's great OCR library, high accuracy and easy to use. You can check it out 
[EasyOCR](https://github.com/JaidedAI/EasyOCR)

## Thank you Ollama for API runtime 🤖
Ollama is a great platform for run LLM model. You can check it out
[Ollama](https://ollama.com/)

## Thank you Google for Model 🤖
Gemma2 is developed by Google. This is the best model for dialogue translation that I researched. You can check.
[Gemma2](https://ollama.com/library/gemma2)

## License 🔑

Distributed under the MIT License. See [LICENSE](https://github.com/kang49/deepalogue/blob/main/LICENSE) for more information.

## Project Founder 😎

* **kang49 | Meta_Keen | Kankawee Aramrak** - *Software Engineer at TensorMiK* - [Github](https://github.com/kang49)


<p align="center">
    Made with 💖 by Meta_Keen
</p>
