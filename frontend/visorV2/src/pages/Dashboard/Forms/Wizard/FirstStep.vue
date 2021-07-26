<template>
  <ValidationObserver ref="form">
    <form @submit.prevent="validate">
      <h5 class="info-text">
        Let's start with the basic information (with validation)
      </h5>
      <div class="row justify-content-center">
        <div class="col-sm-4">
          <div class="picture-container">
            <el-upload
              class="picture"
              action="https://jsonplaceholder.typicode.com/posts/"
              :on-change="handlePreview"
              :auto-upload="false"
              :show-file-list="false"
            >
              <img v-if="imageUrl" :src="imageUrl" class="picture-src" />
            </el-upload>
            <h6 class="description">Choose Picture</h6>
          </div>
        </div>
        <div class="col-sm-6">
          <ValidationProvider
            name="firstName"
            rules="required"
            v-slot="{ passed, failed }"
          >
            <fg-input
              type="text"
              :error="failed ? 'The First name field is required' : null"
              :hasSuccess="passed"
              class="form-control-lg"
              placeholder="First Name (required)"
              v-model="firstName"
              addon-left-icon="now-ui-icons users_circle-08"
            >
            </fg-input>
          </ValidationProvider>

          <ValidationProvider
            name="lastName"
            rules="required"
            v-slot="{ passed, failed }"
          >
            <fg-input
              class="form-control-lg"
              :error="failed ? 'The Last name field is required' : null"
              :hasSuccess="passed"
              placeholder="Last Name (required)"
              v-model="lastName"
              addon-left-icon="now-ui-icons text_caps-small"
            >
            </fg-input>
          </ValidationProvider>
        </div>
        <div class="col-12 col-sm-10 mt-3">
          <ValidationProvider
            name="email"
            rules="required|email"
            v-slot="{ passed, failed }"
          >
            <fg-input
              class="form-control-lg"
              :error="failed ? 'The Email field is required' : null"
              :hasSuccess="passed"
              name="email"
              placeholder="Email (required)"
              v-model="email"
              addon-left-icon="now-ui-icons text_caps-small"
            >
            </fg-input>
          </ValidationProvider>
        </div>
      </div>
    </form>
  </ValidationObserver>
</template>
<script>
import { Upload } from "element-ui";
import { extend } from "vee-validate";
import { required, email } from "vee-validate/dist/rules";

extend("required", required);
extend("email", email);

export default {
  components: {
    [Upload.name]: Upload
  },
  data() {
    return {
      firstName: "",
      lastName: "",
      email: "",
      imageUrl: "img/default-avatar.png"
    };
  },
  methods: {
    handlePreview(file) {
      this.model.imageUrl = URL.createObjectURL(file.raw);
    },
    validate() {
      return this.$refs.form.validate().then(res => {
        this.$emit("on-validated", res);
        return res;
      });
    }
  }
};
</script>
<style></style>
