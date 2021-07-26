<template>
  <ValidationObserver v-slot="{ handleSubmit }">
    <form @submit.prevent="handleSubmit(submit)">
      <card no-footer-line>
        <div slot="header">
          <h4 class="card-title">
            Register Form
          </h4>
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
              label="Email address"
              name="email"
              v-model="email"
            >
            </fg-input>
          </ValidationProvider>

          <ValidationProvider
            vid="confirmation"
            rules="required"
            v-slot="{ passed, failed }"
          >
            <fg-input
              type="password"
              :error="failed ? 'The Password field is required' : null"
              :hasSuccess="passed"
              name="password"
              label="Password"
              v-model="password"
            >
            </fg-input>
          </ValidationProvider>

          <ValidationProvider
            name="password"
            rules="required|confirmed:confirmation"
            v-slot="{ passed, failed }"
          >
            <fg-input
              type="password"
              :error="failed ? 'The Password does not match' : null"
              :hasSuccess="passed"
              name="confirmation"
              label="Confirm Password"
              v-model="confirmation"
            >
            </fg-input>
          </ValidationProvider>
          <div class="category form-category">* Required fields</div>
        </div>
        <div slot="footer" class="text-right">
          <checkbox v-model="subscribe" class="pull-left" name="subscribe">
            Subscribe to newsletter
          </checkbox>

          <n-button native-type="submit" type="primary">Register</n-button>
        </div>
      </card>
    </form>
  </ValidationObserver>
</template>
<script>
import { extend } from "vee-validate";
import { required, email, confirmed } from "vee-validate/dist/rules";

extend("email", email);
extend("required", required);
extend("confirmed", confirmed);

import { Checkbox } from "src/components/index";

export default {
  components: {
    Checkbox
  },
  data() {
    return {
      email: "",
      password: "",
      confirmation: "",
      subscribe: false
    };
  },
  methods: {
    submit() {
      alert("Form has been submitted!");
    }
  }
};
</script>
<style></style>
