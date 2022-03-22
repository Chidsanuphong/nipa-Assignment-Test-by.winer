<template> 
  <v-container>
    <p class="display-2 font-weight-thin center">Pending</p>
    <v-card style="max-width: 1000px; ">
    <v-card-title >
      <span class="headline">All Tickets waiting to be accepted</span>
      <v-spacer></v-spacer>
      
      <div class="search-wrapper">
        
        <v-text-field
          v-model="search"
          append-icon="search"
          label="Search"
          color="pink lighten-3"
          hide-details
        ></v-text-field>
      </div>
        
    </v-card-title>
    </v-card>
    <v-card style="max-width: 1000px;" class="mt-6"  v-model="search"
    v-for="(item,index) in order" :key="index"> 
      <v-layout row wrap >
        <v-flex md1 >
          <div class="grey--text">Title</div>
          <v-card-text class="justify-start">{{item.title}}</v-card-text>
        </v-flex>
        <v-flex md3>
          <div class="grey--text">Description</div>
          <v-card-text class="justify-start">{{item.description}}</v-card-text>
        </v-flex>
        <v-flex md2>
          <div class="grey--text">information</div>
          <v-card-text class="justify-start">{{item.information}}</v-card-text>
        </v-flex>
        <v-flex md2>
          <div class="grey--text">Timestamp</div>
          <v-card-text class="justify-start">{{item.timestamps}}</v-card-text>
        </v-flex>
        <v-flex md2>
          <div class="grey--text">Status</div>
          <v-card-text class="justify-start">{{item.staus}}</v-card-text>
        </v-flex>
        <v-flex md2 >
          <div class="grey--text">Edit / Delete</div>
          <v-card-text class="justify-start">
          <v-icon
              small
              class="mr-2" color="warning"
              @click="edited(index)"
            >
              edit
            </v-icon>
            <v-icon
              small color="error"
              @click="deleteOrder(index)"
            >
              delete
            </v-icon>
          </v-card-text>
        </v-flex>
      </v-layout>
    </v-card>
    <!-- <v-data-table
      :headers="headers"
      :items="order"
      
      disable-pagination
      :hide-default-footer="true"
    >     
      </v-data-table> -->
            <!-- <template v-slot:[`item.actions`]=" {item} ">
              <td class="justify-space-around layout">
                <v-icon
                  color="light-green accent-4"
                  class="mr-2"
                  @click="submitTicket(item)"
                >
                  done
                </v-icon>
                <v-icon
                  small
                  color="warning"
                  class="mr-2"
                  @click="editedTicket(item)"
                >
                  edit
                </v-icon>
                <v-icon
                  color="error"
                  @click="deletes"
                >
                  delete
                </v-icon>
              </td>
            </template> -->
    <v-dialog v-model="dialog1" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="headline">Edit Ticket</span>
      <v-spacer></v-spacer>
      <v-btn color="light-green accent-4" rounded outlined @click="acceptedTicket">Accept</v-btn>
        </v-card-title>
        <v-card-text>
          <v-container grid-list-md>
            <v-layout wrap>
                <v-flex md12>
                  <v-text-field
                    v-model="edit.title"
                    label="Name"
                    clearable color="pink lighten-3"
                  ></v-text-field>
                </v-flex>
                <v-flex md12>
                  <v-text-field
                    v-model="edit.description"
                    label="Department"
                    clearable color="pink lighten-3"
                  ></v-text-field> 
                </v-flex>
                <v-flex md12>
                  <v-text-field
                    v-model="edit.information"
                    label="Tel"
                    clearable color="pink lighten-3"
                  ></v-text-field>
                </v-flex>  
              <v-flex md12>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn outlined color="pink lighten-3" @click="editedTicket">Save</v-btn>
                  <v-btn outlined color="pink lighten-3" @click="dialog1 = false">Close</v-btn>
                </v-card-actions>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card-text>
      </v-card>
    </v-dialog>   

    <v-dialog v-model="dialog2" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="headline">Do you want to delete this ticket?</span>
        </v-card-title>
        <v-card-text>
          <v-container grid-list-md>
            <v-layout wrap>
              
                <v-flex md12>
                  <h4>Title</h4> <div>{{deleteticket.title}}</div>
                </v-flex>
                <v-flex md12>  
                  <h4>Description</h4> <div>{{deleteticket.description}}</div>
                </v-flex>
                <v-flex md12>
                  <h4>Information</h4><div>{{deleteticket.information}}</div>
                </v-flex>  
                <v-flex md12>
                  <h4>Timestamps</h4><div>{{deleteticket.timestamps}}</div>
                </v-flex>
               
              <v-flex>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn outlined color="error" @click="deletes">Delete</v-btn>
                  <v-btn outlined color="light-green accent-4" @click="dialog2 = false">Close</v-btn>
                </v-card-actions>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card-text>
      </v-card>
    </v-dialog>
    
    
  </v-container>
</template>
<script>
export default {
  name: 'Pending',
  data: () => ({
      search: '',
      order: [],
      deleteticket:[],
      edit:[],
      accepted:[],
      dialog1: false,
      dialog2: false,
      dataedit:{
        id:'',
        title: '',
        description: '',
        information:'',
        timestamps:'',
        updates:'',
        staus:"Resolved"
      },
      get timestamp() {
        const today = new Date();
        const date = today.getDate() + '-' + (today.getMonth()+1) + '-' + today.getFullYear();
        const time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
        const timestamp = date + ' ' + time;
        return timestamp;
      },
    }),
  methods: { 
    getPending(){
      this.axios.get("http://localhost:5000/getuser").then(res => {
        console.log('Order',res.data);
        this.order = res.data
        console.log("order"+this.order);
      })
    },
    deleteOrder(n){
    console.log(this.order[n])
    this.deleteticket = this.order[n]
    this.dialog2 = true
    },
    edited(n){
      this.edit = this.order[n]
      console.log("edit "+this.edit)
      this.dialog1 = true
    },
    editedTicket(){
      this.dataedit.id = this.edit.id
      this.dataedit.title = this.edit.title
      this.dataedit.description = this.edit.description
      this.dataedit.information = this.edit.information
      this.dataedit.timestamps = this.edit.timestamps
      this.dataedit.updates = this.timestamp
      console.log("editedTicket"+this.dataedit)
      this.axios.post("http://localhost:5000/editTicket",this.dataedit).then(res =>{
        console.log("edit success",res.data)
        this.getPending()
      })
      this.dialog1 = false
    },
    
    acceptedTicket(){
      this.accepted = this.edit
      console.log(this.accepted)
      this.axios.post("http://localhost:5000/accepted",this.accepted).then(res =>{
        console.log("accepted",res.data)
      })
      this.dialog1 = false
      this.acceptedOutofPending()
      alert ("Accepted ")

    },
    acceptedOutofPending(){
      this.axios.delete("http://localhost:5000/deletePending/"+this.accepted.id).then
      console.log("delete success")
    },
    deletes(){
      this.axios.delete("http://localhost:5000/deletePending/"+this.deleteticket.id).then
      console.log("delete success")
      this.axios.post("http://localhost:5000/rejected",this.deleteticket).then
      this.getPending()
      this.dialog2 = false
      this.created()
    },
    
  },
  created(){
      this.getPending()
    },
    
}
</script>