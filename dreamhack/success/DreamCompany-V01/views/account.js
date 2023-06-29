const id = document.getElementById("id");
const password = document.getElementById("password");
const btn = document.getElementById("submit_btn");

btn.addEventListener("click", (e) => {
  $.ajax({
    url: "/user/account",
    type: "POST",
    data: {
      id: String(id.value),
      password: String(password.value),
    },
    success: function (data) {
      alert(data.message === undefined ? "no message" : data.message);
      localStorage.setItem("accessToken", data.access);
      location.href = "/";
    },
  });
  console.log("lla")
});