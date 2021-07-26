<template>
  <ValidationObserver v-slot="{ handleSubmit }">
    <form @submit.prevent="handleSubmit(submit)">
      <div class="col-md-4 ml-auto mr-auto">
        <form @submit.prevent="login">
          <card class="card-login card-plain">
            <div slot="header">
              <div class="logo-container">
                <img src="img/now-logo.png" alt="" />
              </div>
            </div>

            <div>
              <ValidationProvider
                name="email"
                rules="required|email"
                v-slot="{ passed, failed }"
              >
                <fg-input
                  type="email"
                  :error="failed ? 'The Email field is required' : null"
                  :hasSuccess="passed"
                  class="no-border form-control-lg"
                  placeholder="Email"
                  addon-left-icon="now-ui-icons ui-1_email-85"
                  v-model="email"
                >
                </fg-input>
              </ValidationProvider>

              <ValidationProvider
                name="password"
                rules="required|min:5"
                v-slot="{ passed, failed }"
              >
                <fg-input
                  type="password"
                  :error="failed ? 'The Password field is required' : null"
                  :hasSuccess="passed"
                  class="no-border form-control-lg"
                  placeholder="Password"
                  addon-left-icon="now-ui-icons ui-1_lock-circle-open"
                  v-model="password"
                >
                </fg-input>
              </ValidationProvider>
            </div>

            <div slot="footer">
              <n-button native-type="submit" type="primary" round block>
                Get Started
              </n-button>
              <div class="pull-left">
                <h6>
                  <router-link class="link footer-link" to="/register">
                    Create Account
                  </router-link>
                </h6>
              </div>

              <div class="pull-right">
                <h6>
                  <a href="#pablo" class="link footer-link">Need Help?</a>
                </h6>
              </div>
            </div>
          </card>
        </form>
      </div>
    </form>
  </ValidationObserver>
</template>
<script>
import { extend } from "vee-validate";
import { required, email, min } from "vee-validate/dist/rules";

extend("email", email);
extend("required", required);
extend("min", min);

export default {
  name: "login",
  data() {
    return {
      email: "",
      password: ""
    };
  },
  methods: {
    async login() {
      let isValidForm = await this.$validator.validate();
      if (isValidForm) {
        // TIP use this.model to send it to api and perform login call
      }
    },
    submit() {
      alert("Form has been submitted!");
    }
  }
};
</script>
<style>
.navbar-nav .nav-item p {
  line-height: inherit;
  margin-left: 5px;
}
</style>
