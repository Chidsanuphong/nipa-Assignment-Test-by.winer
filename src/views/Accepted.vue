<template> 
  <v-container>
    <p class="display-2 font-weight-thin center">Accepted</p>
    <v-card style="max-width: 900px; ">
     <v-card-title >
      <span class="headline">All Tickets is accepted</span>
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
  name: 'Accepted',
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
    getPending(){
      this.axios.get("http://localhost:5000/getAccepted").then(res => {
        this.order = res.data
      })
    },
  },
  created(){
      this.getPending()
    },
}
</script>