new Vue({
    el: "#app",
    data: {
        message: '',
        len: ''
    },
    computed: {
        quants() {

            return this.message

        },

        lengths() {
            if (this.quants === 1) {
                return "length of your password"
            } else {
                return `length of your ${this.quants} passwords`
            }
        },
        showi() {
            return this.message != ''
        }
    },


})