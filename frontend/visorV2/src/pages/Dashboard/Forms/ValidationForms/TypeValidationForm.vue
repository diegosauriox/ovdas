<template>
  <ValidationObserver v-slot="{ handleSubmit }">
    <form @submit.prevent="handleSubmit(submit)" class="form-horizontal">
      <card>
        <h4 slot="header" class="card-title">
          Type Validation
        </h4>
        <div>
          <div class="row">
            <label class="col-sm-2 col-form-label">Requred Text</label>
            <div class="col-sm-7">
              <ValidationProvider
                name="required"
                rules="required"
                v-slot="{ passed, failed }"
              >
                <fg-input
                  type="text"
                  :error="failed ? 'The Required text field is required' : null"
                  :hasSuccess="passed"
                  v-model="required"
                >
                </fg-input>
              </ValidationProvider>
            </div>
            <label class="col-sm-3 label-on-right"
              ><code>required="true"</code></label
            >
          </div>

          <div class="row">
            <label class="col-sm-2 col-form-label">Email</label>
            <div class="col-sm-7">
              <ValidationProvider
                name="email"
                rules="required|email"
                v-slot="{ passed, failed }"
              >
                <fg-input
                  type="email"
                  :error="failed ? 'The Email field is required' : null"
                  :hasSuccess="passed"
                  v-model="email"
                >
                </fg-input>
              </ValidationProvider>
            </div>
            <label class="col-sm-3 label-on-right"
              ><code>email="true"</code></label
            >
          </div>

          <div class="row">
            <label class="col-sm-2 col-form-label">Number</label>
            <div class="col-sm-7">
              <ValidationProvider
                name="number"
                rules="required|numeric"
                v-slot="{ passed, failed }"
              >
                <fg-input
                  type="number"
                  :error="failed ? 'The Numeric field is required' : null"
                  :hasSuccess="passed"
                  v-model="number"
                >
                </fg-input>
              </ValidationProvider>
            </div>
            <label class="col-sm-3 label-on-right"
              ><code>numeric="true"</code></label
            >
          </div>

          <div class="row">
            <label class="col-sm-2 col-form-label">Url</label>
            <div class="col-sm-7">
              <ValidationProvider
                name="url"
                :rules="{
                  required: true,
                  regex: /(https?:\/\/(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9])(:?\d*)\/?([a-z_\/0-9\-#.]*)\??([a-z_\/0-9\-#=&]*)/g
                }"
                v-slot="{ passed, failed }"
              >
                <fg-input
                  type="url"
                  :error="failed ? 'The Url field is required' : null"
                  :hasSuccess="passed"
                  v-model="url"
                >
                </fg-input>
              </ValidationProvider>
            </div>
            <label class="col-sm-3 label-on-right"
              ><code>url="true"</code></label
            >
          </div>

          <div class="row">
            <label class="col-sm-2 col-form-label">Equal To</label>
            <div class="col-sm-3">
              <ValidationProvider
                name="equalTo"
                rules="required"
                vid="confirmation"
                v-slot="{ passed, failed }"
              >
                <fg-input
                  type="text"
                  :error="failed ? 'The EqualTo field is required' : null"
                  placeholder="Source field"
                  :hasSuccess="passed"
                  v-model="equalTo"
                >
                </fg-input>
              </ValidationProvider>
            </div>
            <div class="col-sm-3">
              <ValidationProvider
                name="equal"
                rules="required|confirmed:confirmation"
                v-slot="{ passed, failed }"
              >
                <fg-input
                  type="text"
                  :error="failed ? 'The EqualToSource does not match' : null"
                  placeholder="Destination field"
                  :hasSuccess="passed"
                  v-model="equal"
                >
                </fg-input>
              </ValidationProvider>
            </div>

            <label class="col-sm-4 label-on-right"
              ><code>confirmed="equalToSource"</code></label
            >
          </div>
        </div>
        <div class="text-center">
          <n-button native-type="submit" type="primary"
            >Validate inputs</n-button
          >
        </div>
      </card>
    </form>
  </ValidationObserver>
</template>
<script>
import { extend } from "vee-validate";
import { required, numeric, regex, confirmed } from "vee-validate/dist/rules";

extend("required", required);
extend("numeric", numeric);
extend("regex", regex);
extend("confirmed", confirmed);

export default {
  data() {
    return {
      required: "",
      email: "",
      number: "",
      url: "",
      equal: "",
      equalTo: ""
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
