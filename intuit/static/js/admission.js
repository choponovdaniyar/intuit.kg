const admission__btn = document.querySelector(".admission__btn");
const admission__name = document.querySelector(".admission__name");
const admission__phone = document.querySelector(".admission__phone");

const postAdmissionResponse = async () => {
  const response = await fetch("http://localhost:3200/registration", {
    method: "POST",
    body: JSON.stringify({
      name: admission__name.value,
      phone: admission__phone.value,
      thetext: "Он хочет записаться на день открытых дверей",
    }),
    headers: {
      "Content-Type": "application/json",
    },
  });
  const data = await response.json();
};

admission__btn.addEventListener("click", () => {
  postAdmissionResponse();
});
