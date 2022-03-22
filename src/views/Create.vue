<template> 
  <v-container>
    <p class="display-2 font-weight-thin center">Create</p>
    <v-card style="max-width: 600px;">
      <v-card-title>
          <span class="headline" font-weight-thin >Add New Ticket</span>
      </v-card-title>
      <v-card-text>
        <v-container grid-list-md>

          <v-layout wrap>
            <v-flex md12 xs12>
              <v-text-field v-model="data.title" label="Title" color="pink lighten-3" :rules="rules"></v-text-field>
            </v-flex>
            <v-flex md12 xs12>
              <v-text-field v-model="data.description" label="Description" color="pink lighten-3" :rules="rules"></v-text-field>
            </v-flex>
            <v-flex md12 xs12>
              <v-text-field v-model="data.information" label="Contact information" color="pink lighten-3" :rules="rules"></v-text-field>
            </v-flex>
            <v-flex md12 xs12>
              <v-text-field v-model="timestamp" label="Timestamp" color="pink lighten-3" readonly outlined></v-text-field>
            </v-flex>
            <v-flex md12 xs12>
              <v-text-field v-model="timestamp" label="Latest ticket update timestamp" color="pink lighten-3" readonly outlined></v-text-field>
            </v-flex>
            <v-flex md12 xs12>
              <v-text-field value="Pending" label="Status" color="pink lighten-3" readonly outlined></v-text-field>
            </v-flex>
            
          </v-layout>

              <v-flex >
                <v-card-actions class="d-flex justify-space-around mb-6">
                  <div class="text-center">
                  <v-btn style="width: 100px;" class="ma-2" color="pink lighten-3" rounded outlined @click="submit">Save</v-btn>
                  <v-btn style="width: 100px;" class="ma-2" color="pink lighten-3" rounded outlined @click="cancel">Cancel</v-btn>
                  </div>
                </v-card-actions>
              </v-flex>

        </v-container>
      </v-card-text>
   </v-card>
  </v-container>
</template>
<script>
export default {
  name: 'Create',
  data: () => ({
    data:{
      title:'',
      description:'',
      information:'',
      timestamp:'',
      update:'',
      staus:''
    },
  get timestamp() {
    const today = new Date();
    const date = today.getDate() + '-' + (today.getMonth()+1) + '-' + today.getFullYear();
    const time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    const timestamp = date + ' ' + time;
    return timestamp;
  },
  rules: [
        value => !!value || 'Required.',
      ],
    }),
  methods: {
    submit(){
      this.data.timestamp = this.timestamp
      this.data.update = this.timestamp
      this.data.staus = 'Pending'
      console.log(this.data)
      this.axios.post("http://localhost:5000/addPending",this.data).then
      alert ("Success")
    },
    cancel(){
      this.data.title = ''
      this.data.description = ''
      this.data.information = ''
    },
  },
}
</script>