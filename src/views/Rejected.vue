<template> 
  <v-container>
    <p class="display-2 font-weight-thin center">Rejected</p>
    <v-card style="max-width: 800px; ">
     <v-card-title >
      <span class="headline">All Tickets is rejected</span>
      <v-data-table
      :headers="headers"
      :items="order"
      disable-pagination
    >
      </v-data-table>
     </v-card-title> 
    </v-card>
  </v-container>
</template>
<script>
export default {
  name: 'Rejected',
  data: () => ({
      order: [],
      headers: [
          {
            text: 'Title',
            value: 'title'
            
          },
          {
            text: 'Description',
            value: 'description'
          },
          {
            text: 'Information',
            value: 'information'
          },
          {
            text: 'Timestamps',
            value: 'timestamps'
          },
          {
            text: 'Time update',
            value: 'updates'
          },
          {
            text: 'Staus',
            value: 'staus'
          },
          
        ],
    }),
  methods: {
    getRejected(){
      this.axios.get("http://localhost:5000/getRejected").then(res => {
        this.order = res.data
      })
    },
  },
  created(){
      this.getRejected()
    },
}
</script>