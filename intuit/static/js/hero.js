const hero__btn = document.querySelector(".hero__btn");
const hero__name = document.querySelector(".hero__name");
const hero__phone = document.querySelector(".hero__phone");

const postMailResponse = async () => {
  const response = await fetch("http://localhost:3200/registration", {
    method: "POST",
    body: JSON.stringify({
      name: hero__name.value,
      phone: hero__phone.value,
      thetext: "Он хочет узнать минимальный проходной балл"
    }),
    headers: {
      "Content-Type": "application/json",
    },
  });
  const data = await response.json();
};

hero__btn.addEventListener("click", () => {
    postMailResponse();
});
