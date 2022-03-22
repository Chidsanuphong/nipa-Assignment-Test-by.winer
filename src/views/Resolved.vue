<template> 
  <v-container>
    <p class="display-2 font-weight-thin center">Resolved</p>
    <v-card style="max-width: 850px; ">
     <v-card-title >
      <span class="headline">All Tickets is resolved</span>
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
  name: 'Resolved',
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
    getResolved(){
      this.axios.get("http://localhost:5000/getResolved").then(res => {
        this.order = res.data
    })
    },
  },
  created(){
      this.getResolved()
    },
}
</script>