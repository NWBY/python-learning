<template>
    <div>
        <button @click="showModal" class="bg-blue-500 text-white py-2 px-8 rounded">New Token</button>
        <Modal v-show="show" @close="show = false">
            <template v-slot:header>
                <p>New Token</p>
            </template>
            <template v-slot:body>
                <form>
                    <div class="flex flex-col my-2">
                        <label for="name">Name</label>
                        <input type="text" id="name" name="name" v-model="form.name">
                    </div>
                    <div class="flex flex-col my-2">
                        <label for="unit_name">Unit Name</label>
                        <input type="text" id="unit_name" name="unit_name" v-model="form.unit_name">
                    </div>
                    <div class="flex flex-col my-2">
                        <label for="total_supply">Total Supply</label>
                        <input type="text" id="total_supply" name="total_supply" v-model="form.total_supply">
                    </div>
                    <div>
                        <button @click="submit" class="bg-blue-500 text-white py-2 w-full rounded">Submit</button>
                    </div>
                </form>
            </template>
        </Modal>
    </div>
</template>

<script>
import axios from 'axios';

import Modal from '../utility/Modal.vue';

export default {
    components: {
        Modal,
    },
    data() {
        return {
            show: false,
            form: {
                name: '',
                unit_name: '',
                total_supply: ''
            }
        };
    },
    methods: {
        showModal() {
            this.show = true;
        },
        submit() {
            axios.post(`${apiUrl}/tokens/`, this.form).then((res) => {
                this.show = false;
                this.$emit('submitted')
            }).catch((err) => {
                
            });
        }
    },
};
</script>

<style>
input {
    @apply border-2 border-blue-500 rounded p-1;
}
</style>
