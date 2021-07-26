<template>
  <div class="places-sweet-alerts">
    <div class="row">
      <div class="col-md-3 ml-auto">
        <card>
          <div class="text-center">
            <p class="card-text">Basic example</p>
            <n-button type="primary" @click.native="showSwal('basic')"
              >Try me!</n-button
            >
          </div>
        </card>
        <card>
          <div class="text-center">
            <p class="card-text">Custom HTML description</p>
            <n-button type="primary" @click.native="showSwal('custom-html')"
              >Try me!</n-button
            >
          </div>
        </card>
        <card>
          <div class="text-center">
            <p class="card-text">Modal window with input field</p>
            <n-button type="primary" @click.native="showSwal('input-field')"
              >Try me!</n-button
            >
          </div>
        </card>
        <card>
          <div class="text-center">
            <p class="card-text">
              A message with auto close timer set to 2 seconds
            </p>
            <n-button type="primary" @click.native="showSwal('auto-close')"
              >Try me!</n-button
            >
          </div>
        </card>
      </div>
      <div class="col-md-3 mr-auto">
        <card>
          <div class="text-center">
            <p class="card-text">A success message</p>
            <n-button type="primary" @click.native="showSwal('success-message')"
              >Try me!</n-button
            >
          </div>
        </card>
        <card>
          <div class="text-center">
            <p class="card-text">
              A warning message, with a function attached to the "Confirm"
              Button...
            </p>
            <n-button
              type="primary"
              @click.native="showSwal('warning-message-and-confirmation')"
              >Try me!</n-button
            >
          </div>
        </card>
        <card>
          <div class="text-center">
            <p class="card-text">A title with a text under</p>
            <n-button type="primary" @click.native="showSwal('title-and-text')"
              >Try me!</n-button
            >
          </div>
        </card>
        <card>
          <div class="text-center">
            <p class="card-text">
              ...and by passing a parameter, you can execute something else for
              "Cancel"
            </p>
            <n-button
              type="primary"
              @click.native="showSwal('warning-message-and-cancel')"
              >Try me!</n-button
            >
          </div>
        </card>
      </div>
    </div>
  </div>
</template>
<script>
import Swal from "sweetalert2";
export default {
  methods: {
    showSwal(type) {
      if (type === "basic") {
        Swal.fire({
          title: `Here's a message!`,
          buttonsStyling: false,
          confirmButtonClass: "btn btn-success"
        });
      } else if (type === "title-and-text") {
        Swal.fire({
          title: `Here's a message!`,
          text: `It's pretty, isn't it?`,
          buttonsStyling: false,
          confirmButtonClass: "btn btn-info"
        });
      } else if (type === "success-message") {
        Swal.fire({
          title: `Good job!`,
          text: "You clicked the button!",
          buttonsStyling: false,
          confirmButtonClass: "btn btn-success",
          type: "success"
        });
      } else if (type === "warning-message-and-confirmation") {
        Swal.fire({
          title: "Are you sure?",
          text: `You won't be able to revert this!`,
          type: "warning",
          showCancelButton: true,
          confirmButtonClass: "btn btn-success",
          cancelButtonClass: "btn btn-danger",
          confirmButtonText: "Yes, delete it!",
          buttonsStyling: false
        }).then(result => {
          if (result.value) {
            Swal.fire({
              title: "Deleted!",
              text: "Your file has been deleted.",
              type: "success",
              confirmButtonClass: "btn btn-success",
              buttonsStyling: false
            });
          }
        });
      } else if (type === "warning-message-and-cancel") {
        Swal.fire({
          title: "Are you sure?",
          text: "You will not be able to recover this imaginary file!",
          type: "warning",
          showCancelButton: true,
          confirmButtonText: "Yes, delete it!",
          cancelButtonText: "No, keep it",
          confirmButtonClass: "btn btn-success",
          cancelButtonClass: "btn btn-danger",
          buttonsStyling: false
        }).then(result => {
          if (result.value) {
            Swal.fire({
              title: "Deleted!",
              text: "Your imaginary file has been deleted.",
              type: "success",
              confirmButtonClass: "btn btn-success",
              buttonsStyling: false
            });
          } else if (result.dismiss === Swal.DismissReason.cancel) {
            Swal.fire({
              title: "Cancelled",
              text: "Your imaginary file is safe :)",
              type: "error",
              confirmButtonClass: "btn btn-info",
              buttonsStyling: false
            });
          }
        });
      } else if (type === "custom-html") {
        Swal.fire({
          title: "HTML example",
          buttonsStyling: false,
          confirmButtonClass: "btn btn-success",
          html: `You can use <b>bold text</b>,
            <a href="http://github.com">links</a>
            and other HTML tags`
        });
      } else if (type === "auto-close") {
        Swal.fire({
          title: "Auto close alert!",
          text: "I will close in 2 seconds.",
          timer: 2000,
          showConfirmButton: false
        });
      } else if (type === "input-field") {
        Swal.fire({
          title: "Input something",
          html: `<div class="form-group">
            <input id="input-field" type="text" class="form-control" />
            </div>`,
          showCancelButton: true,
          confirmButtonClass: "btn btn-success",
          cancelButtonClass: "btn btn-danger",
          buttonsStyling: false
        }).then(() => {
          Swal.fire({
            type: "success",
            html:
              "You entered: <strong>" +
              document.getElementById("input-field").value +
              "</strong>",
            confirmButtonClass: "btn btn-success",
            buttonsStyling: false
          });
        });
      }
    }
  }
};
</script>
<style>
.el-dialog {
  width: 50%;
}

@media (max-width: 800px) {
  .el-dialog {
    width: 90%;
  }
}
</style>
