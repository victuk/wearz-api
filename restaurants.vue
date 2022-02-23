<template>

  <div>
    <a-page-header sub-title="Restaurant">
      <template slot="extra">
        <a-button type="primary" @click="visible = true">Add Restaurant</a-button>
      </template>
    </a-page-header>

    <RestaurantTable :newRestaurant="newRestaurant" />

    <a-modal v-model="visible" title="Add Category" @ok="addRestaurant">
      <template slot="footer">
        <a-button key="back" @click="reset">Cancel</a-button>
        <a-button key="submit" type="primary" :loading="loading">Submit</a-button>
      </template>
      <a-form-model
        ref="restaurantForm"
        :model="details"
        :rules="rules"
        :label-col="labelCol"
        :wrapper-col="wrapperCol"
        layout="horizontal"
      >
        <a-row>
          <a-col :md="{ span: 22, offset: 1 }">
            <a-form-model-item label="Restaurant Name" prop="name">
              <a-input v-model="details.name" placeholder="Restaurant Name"/>
            </a-form-model-item>
          </a-col>
          <a-col :md="{ span: 22, offset: 1 }">
            <a-form-model-item label="Description" prop="description">
              <a-input v-model="details.description" placeholder="Restaurant Short Description"/>
            </a-form-model-item>
          </a-col>
          <a-col :md="{ span: 22, offset: 1 }">
            <a-form-model-item label="Phone" prop="phone">
              <a-input v-model="details.phone" placeholder="Phone"/>
            </a-form-model-item>
          </a-col>
          <a-col :md="{ span: 22, offset: 1 }">
            <a-form-model-item label="State" prop="state">
              <a-select v-model="details.state" placeholder="State">
                <a-select-option v-for="(state, i) in states" :key="i" :value="state.state.name">
                  {{ state.state.name }}
                </a-select-option>
              </a-select>
            </a-form-model-item>
          </a-col>
          <a-col :md="{ span: 22, offset: 1 }">
            <a-form-model-item label="LGA" prop="lga">
              <a-select v-model="details.lga">
                <a-select-option v-for="(lga, i) in lgas" :key="i" :value="lga.name">
                  {{ lga.name }}
                </a-select-option>
              </a-select>
            </a-form-model-item>
          </a-col>

          <a-col :md="{ span: 22, offset: 1 }">
            <a-form-model-item label="City" prop="city">
              <a-input v-model="details.city" placeholder="City"/>
            </a-form-model-item>
          </a-col>

          <a-col :md="{ span: 22, offset: 1 }">
            <a-form-model-item label="Address" prop="address">
              <a-input v-model="details.address" placeholder="address"/>
            </a-form-model-item>
          </a-col>
          <a-col :md="{ span: 22, offset: 1 }">
            <a-form-model-item label="Landmark" prop="landmark">
              <a-input v-model="details.landmark" placeholder="landmark"/>
            </a-form-model-item>
          </a-col>
          <a-col :md="{ span: 22, offset: 1 }">
            <a-form-model-item label="Delivery Time" prop="deliveryTime">
              <a-input v-model="details.deliveryTime" placeholder="deliveryTime"/>
            </a-form-model-item>
          </a-col>
          <a-col :md="{ span: 10, offset: 1 }">
            <a-form-model-item label="Latitude" prop="lat">
              <a-input v-model="details.lat" placeholder="Lat"/>
            </a-form-model-item>
          </a-col>
          <a-col :md="{ span: 10, offset: 1 }">
            <a-form-model-item label="Longitude" prop="lng">
              <a-input v-model="details.lng" placeholder="Lng"/>
            </a-form-model-item>
          </a-col>
          <a-col :md="{ span: 10, offset: 1 }">
            <a-upload list-type="picture" :default-file-list="fileList" :remove="handleRemove" :before-upload="beforeUpload">
              <a-button> <a-icon type="upload" /> Upload Picture </a-button>
            </a-upload>
          </a-col>

        </a-row>
        <a-row>
        </a-row>
      </a-form-model>
    </a-modal>
  </div>

</template>

<script>
  import upload from '@/mixins/upload'
  import states from '@/data/states.json'
  import countries from '@/data/countries.json'
  import RestaurantTable from '@/components/dashboard/restaurant/RestaurantTable'

  export default {
    name: 'AddRestaurant',
    components: {
      RestaurantTable
    },
    layout: 'dashboard',
    mixins: [upload],
    data() {
      return {
        countries,
        states,
        lgas: '',
        newRestaurant: '',
        restaurants: '',
        file: '',
        visible: false,
        loading: false,
        labelCol: { span: 24 },
        wrapperCol: { span: 24 },
        fileList: [],
        details: {
          name: '',
          description: '',
          phone: '',
          imagePath: '',
          state: '',
          lga: '',
          city: '',
          landmark: '',
          address: '',
          deliveryTime: '',
          lat: '',
          lng: '',
        },
        rules: {
          name: [
            {required: true, message: 'Name is required', trigger: 'change'},
            {min: 6, message: 'Length should not be less than 6', trigger: 'change'},
          ],
          description: [
            {required: true, message: 'Description is required', trigger: 'change'},
            {min: 6, message: 'Length should not be less than 6', trigger: 'change'},
          ],
          phone: [
            {required: true, message: 'Phone is required', trigger: 'change'},
            {min: 6, message: 'Length should not be less than 6', trigger: 'change'},
            {integer: true, message: 'Invalid Phone entered', trigger: 'change'},
          ]
        }
      }
    },
    methods: {
      handleRemove(file) {
        const index = this.fileList.indexOf(file);
        const newFileList = this.fileList.slice();
        newFileList.splice(index, 1);
        this.fileList = newFileList;
      },
      beforeUpload(file) {
        this.fileList = [...this.fileList, file];
        return false;
      },
      async addRestaurant() {

        this.$refs.restaurantForm.validate(async valid => {

          if (valid) {
            this.loading = true
            const { fileList } = this;
            this.details.imagePath = (await this.saveFile(fileList[0])).secure_url;
            const res = await this.$axios.$post('vendor/restaurant', this.details);

            if (res.success) {
              this.loading = false
              this.newRestaurant = res.data;
              this.reset()
              this.$message.success('Restaurant added successfully')
            }
          } else {
            this.loading = false
            this.$message.error('Error occurred')
          }
        })
      },
      async addFile(e) {
        this.file = e
      },
      reset() {
        this.details = {}
        this.fileList = [];
        this.file = '';
        this.visible = false;
      },

      getLgas(state) {
        if (state) {
          this.lgas = (this.states.find(item => item.state['name'] == state)).state.locals
        }
      },
    },

    watch: {
      'details.state': {
        handler: function (val) {
          this.getLgas(val)
        }
      }
    }
  }
</script>

<style scoped>

</style>
