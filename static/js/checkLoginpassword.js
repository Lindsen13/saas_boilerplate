function loginSuccess() {
  toastr.success("Redirecting you to the dashboard")
  window.location.href = "/"
}

$("#login").submit(function () {
  $("#button").prop("disabled", true)
  $("#img").show()
  event.preventDefault()
  $.ajax({
    url: "/check_login_password",
    data: $(this).serialize(),
    type: "POST",
    success: function (response) {
      $("#img").hide()
      if (response === "true") {
        setTimeout(loginSuccess, 5000)
        swal
          .fire({
            icon: "success",
            title: "Login Successful",
          })
          .then((result) => {
            window.location.href = "/"
          })
      } else {
        swal
          .fire({
            icon: "error",
            title: "Login Error",
            text: "Incorrect Username or password",
          })
          .then((result) => {
            $("#button").removeAttr("disabled")
          })
      }
    },
    error: function (error) {
      console.log(error)
    },
  })
})
