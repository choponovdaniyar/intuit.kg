window.onload = function () {
  let result = [];
  let step = 0;
  let inputStep = 1;

  function showQuestion(questionNumber) {
    document.querySelector(".question").innerHTML = quiz[step]["q"];
    let answer = "";
    for (let key in quiz[step]["a"]) {
      answer += `<li class="quiz__item"><button data-v="${key}" class="quiz__variant">${quiz[step]["a"][key]}</button> </li>`;
    }

    document.querySelector(".answer").innerHTML = answer;
  }

  document.onclick = function (event) {
    event.stopPropagation();
    if (
      event.target.classList.contains("quiz__variant") &&
      step < quiz.length
    ) {
      if (event.target.innerHTML != undefined) {
        result.push(event.target.innerHTML);
        document.querySelector(`.quiz${inputStep}`).value =
          event.target.innerHTML;
      }
      step++;
      inputStep++;
      console.log(document.querySelector(`.quiz${step}`));
      if (step + 1 == quiz.length + 1) {
        document.querySelector(".question").remove();
        document.querySelector(".answer").remove();
        showResult();
      } else {
        showQuestion(step);
      }
    }
  };

  function showResult() {
    let key = Object.keys(result).reduce(function (a, b) {
      return result[a] > result[b] ? a : b;
    });

    document.querySelector(".quiz__form--btn").style.display = "block";
      document
      .querySelectorAll(".quiz__data")
      .forEach((item) => (item.value = ""));
    document
      .querySelectorAll(".quiz__data")
      .forEach((item) => (item.style.display = "block"));

  }

  showQuestion(step);
};
