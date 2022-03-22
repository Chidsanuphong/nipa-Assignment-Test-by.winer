<template>
  <v-app>
    <v-col align="center">
        <v-container>
          <router-view></router-view>
        </v-container>
    </v-col>
    <v-app-bar app color="pink lighten-2" dark elevation="5">
        <v-app-bar-nav-icon @click="drawer=!drawer"/>
        <v-toolbar-title class="headline">
          <span>Nipa Ticket management</span>
        </v-toolbar-title>
        
        <v-spacer></v-spacer>
        <v-tooltip bottom>
          <template v-slot:activator="{on: tooltip}">
            <v-btn icon v-on="{...tooltip}" flat color="white">
              <v-icon>exit_to_app</v-icon>
            </v-btn>
          </template>
        <span>Log out</span>
      </v-tooltip>

          
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" absolute >
    <v-list-item-group color="pink accent-2">


      <v-list-item @click="gotoCreate">
        <v-list-item-icon>
          <v-icon>add</v-icon>
        </v-list-item-icon>

          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
        <v-list-item-title v-bind="attrs" v-on="on" >Create</v-list-item-title>
            </template>
              <span>สร้างตั๋วใหม่</span>
          </v-tooltip>

      </v-list-item>

      <v-list-item @click="gotoPending">
        <v-list-item-icon>
          <v-icon>post_add</v-icon> 
        </v-list-item-icon>
          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
        <v-list-item-title v-bind="attrs" v-on="on" >Pending</v-list-item-title>
            </template>
              <span>รอการอนุมัติ</span>
          </v-tooltip>
      </v-list-item>

      <v-list-item @click="gotoAccepted">
        <v-list-item-icon>
          <v-icon>done</v-icon>
        </v-list-item-icon>
          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
        <v-list-item-title v-bind="attrs" v-on="on" >Accepted</v-list-item-title>
            </template>
              <span>ประวัติการอนุมัติ</span>
          </v-tooltip>
      </v-list-item>

      <v-list-item @click="gotoResolved">
        <v-list-item-icon>
          <v-icon>autorenew</v-icon>
        </v-list-item-icon>  
          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
        <v-list-item-title v-bind="attrs" v-on="on" >Resolved</v-list-item-title>
            </template>
              <span>ประวัติการแก้ไข</span>
          </v-tooltip>
      </v-list-item>

      <v-list-item @click="gotoRejected">
        <v-list-item-icon>
          <v-icon>close</v-icon>
        </v-list-item-icon>
          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
        <v-list-item-title v-bind="attrs" v-on="on" >Rejected</v-list-item-title>
            </template>
              <span>ประวัติการยกเลิก</span>
          </v-tooltip>
      </v-list-item>

    </v-list-item-group>
    </v-navigation-drawer> 
  </v-app>
</template>
<script>
export default {
  name: 'Dash',
  data: () => ({
      drawer: true,
    }),
  methods: {
    gotoCreate () {
      this.$router.push('/create')
    },
    gotoPending () {
      this.$router.push('/pending')
    },
    gotoAccepted () {
      this.$router.push('/accepted')
    },
    gotoResolved () {
      this.$router.push('/resolved')
    },
    gotoRejected () {
      this.$router.push('/rejected')
    },
  },
}
</script>
