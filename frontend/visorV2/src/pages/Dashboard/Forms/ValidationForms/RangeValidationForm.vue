<template>
  <ValidationObserver v-slot="{ handleSubmit }" class="form-horizontal">
    <form @submit.prevent="handleSubmit(submit)">
      <card>
        <h4 slot="header" class="card-title">
          Range Validation
        </h4>
        <div>
          <div class="row">
            <label class="col-sm-2 col-form-label">Min Length</label>
            <div class="col-sm-7">
              <ValidationProvider
                name="minLength"
                rules="required|min:5"
                v-slot="{ passed, failed }"
              >
                <fg-input
                  type="text"
                  :error="failed ? 'The Min Length field is required' : null"
                  :hasSuccess="passed"
                  name="minLength"
                  v-model="minLength"
                >
                </fg-input>
              </ValidationProvider>
            </div>
            <label class="col-sm-3 label-on-right"><code>min="5"</code></label>
          </div>

          <div class="row">
            <label class="col-sm-2 col-form-label">Max Length</label>
            <div class="col-sm-7">
              <ValidationProvider
                name="maxLength"
                rules="required|max:5"
                v-slot="{ passed, failed }"
              >
                <fg-input
                  type="text"
                  :error="failed ? 'The Max Length field is required' : null"
                  :hasSuccess="passed"
                  name="maxLength"
                  v-model="maxLength"
                >
                </fg-input>
              </ValidationProvider>
            </div>
            <label class="col-sm-3 label-on-right"><code>max="5"</code></label>
          </div>

          <div class="row">
            <label class="col-sm-2 col-form-label">Range</label>
            <div class="col-sm-7">
              <ValidationProvider
                name="range"
                rules="required|min:6|max:10"
                v-slot="{ passed, failed }"
              >
                <fg-input
                  type="text"
                  :error="failed ? 'The Range field is required' : null"
                  :hasSuccess="passed"
                  name="range"
                  v-model="range"
                >
                </fg-input>
              </ValidationProvider>
            </div>
            <label class="col-sm-3 label-on-right"
              ><code>min_value="6", max_value="10"</code></label
            >
          </div>

          <div class="row">
            <label class="col-sm-2 col-form-label">Min Value</label>
            <div class="col-sm-7">
              <ValidationProvider
                name="minValue"
                rules="required|min_value:6"
                v-slot="{ passed, failed }"
              >
                <fg-input
                  type="text"
                  :error="failed ? 'The Min Value field is required' : null"
                  :hasSuccess="passed"
                  name="minValue"
                  v-model="minValue"
                >
                </fg-input>
              </ValidationProvider>
            </div>
            <label class="col-sm-3 label-on-right"
              ><code>min_value="6"</code></label
            >
          </div>

          <div class="row">
            <label class="col-sm-2 col-form-label">Max Value</label>
            <div class="col-sm-7">
              <ValidationProvider
                name="maxValue"
                rules="required|max_value:6"
                v-slot="{ passed, failed }"
              >
                <fg-input
                  type="text"
                  :error="failed ? 'The Max Value field is required' : null"
                  :hasSuccess="passed"
                  name="maxValue"
                  v-model="maxValue"
                >
                </fg-input>
              </ValidationProvider>
            </div>
            <label class="col-sm-3 label-on-right"
              ><code>max_value="6"</code></label
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
import {
  required,
  min,
  max,
  min_value,
  max_value
} from "vee-validate/dist/rules";

extend("required", required);
extend("min", min);
extend("max", max);
extend("min_value", min_value);
extend("max_value", max_value);

export default {
  data() {
    return {
      minLength: "",
      maxLength: "",
      range: "",
      minValue: "",
      maxValue: ""
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
