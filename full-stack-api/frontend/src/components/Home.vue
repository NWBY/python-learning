<template>
  <div class="w-2/3 mx-auto">
    <h1 class="text-4xl font-black py-4">Token Tracker</h1>
    <div>
      <div class="flex items-center justify-between mb-4">
        <h3 class="text-2xl font-bold">All Tokens</h3>
        <NewToken @submitted="getTokens"/>
      </div>
      <table class="w-full text-left border border-gray-500/50">
        <thead>
          <th>Name</th>
          <th>Unit Name</th>
          <th>Total Supply</th>
          <th>Market Cap</th>
          <th></th>
        </thead>
        <tbody>
          <tr v-for="token in tokens" :key="token.unit_name">
            <td class="font-semibold">{{token.name}}</td>
            <td>{{token.unit_name}}</td>
            <td>{{humanReadableFormat(token.total_supply)}}</td>
            <td>{{humanReadableFormat(token.market_cap)}}</td>
            <td></td>
          </tr>
        </tbody>
      </table>
      
    </div>
  </div>
</template>

<script>
import axios from 'axios';

import NewToken from './tokens/NewToken.vue';

export default {
  data() {
    return {
      tokens: []
    }
  },
  components: {
    NewToken
  },
  mounted() {
    this.getTokens();
  },
  methods: {
    getTokens() {
      axios.get(`${apiUrl}/tokens/`).then((res) => {
        this.tokens = res.data
        console.log(res.data)
      }).catch((err) => {
        
      });
    },
    humanReadableFormat(num) {
      return num.toLocaleString('en-UK')
    }
  }
}
</script>

<style>
th {
  @apply bg-gray-100 p-2;
}
td {
  @apply p-2;
}
</style>