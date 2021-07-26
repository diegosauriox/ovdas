<template>
  <ValidationObserver ref="form">
    <form @submit.prevent="validate">
      <div class="row justify-content-center">
        <div class="col-sm-12">
          <h5 class="info-text">Are you living in a nice area?</h5>
        </div>
        <div class="col-sm-7">
          <ValidationProvider
            name="streetName"
            rules="required"
            v-slot="{ passed, failed }"
          >
            <fg-input
              label="Street Name"
              v-model="streetName"
              :error="failed ? 'The Street name field is required' : null"
              :hasSuccess="passed"
            >
            </fg-input>
          </ValidationProvider>
        </div>
        <div class="col-sm-3">
          <ValidationProvider
            name="streetNumber"
            rules="required"
            v-slot="{ passed, failed }"
          >
            <fg-input
              label="Street No"
              name="street number"
              v-model="streetNo"
              :error="failed ? 'The Street number field is required' : null"
              :hasSuccess="passed"
            >
            </fg-input>
          </ValidationProvider>
        </div>
        <div class="col-sm-5">
          <ValidationProvider
            name="city"
            rules="required"
            v-slot="{ passed, failed }"
          >
            <fg-input
              label="City"
              :error="failed ? 'The City field is required' : null"
              :hasSuccess="passed"
              name="city"
              v-model="city"
            >
            </fg-input>
          </ValidationProvider>
        </div>
        <div class="col-sm-5">
          <label>Country</label>
          <ValidationProvider
            name="country"
            rules="required"
            v-slot="{ failed }"
          >
            <fg-input :error="failed ? 'The Country field is required' : null">
              <el-select
                v-model="country"
                class="select-primary"
                name="country"
              >
                <el-option
                  v-for="country in countryOptions"
                  class="select-primary"
                  :label="country"
                  :value="country"
                  :key="country"
                ></el-option>
              </el-select>
            </fg-input>
          </ValidationProvider>
        </div>
      </div>
    </form>
  </ValidationObserver>
</template>
<script>
import { Select, Option } from "element-ui";
import { extend } from "vee-validate";
import { required, email } from "vee-validate/dist/rules";

extend("required", required);
extend("email", email);

export default {
  components: {
    [Select.name]: Select,
    [Option.name]: Option
  },
  data() {
    return {
      streetName: "",
      streetNo: "",
      city: "",
      country: "",
      select: null,
      countryOptions: ["One", "Two", "Three", "Four", "Five", "Six"]
    };
  },
  methods: {
    validate() {
      return this.$refs.form.validate().then(res => {
        if (!res) {
          return;
        }
        this.$emit("on-validated", res);
        return res;
      });
    }
  }
};
</script>
<style></style>
