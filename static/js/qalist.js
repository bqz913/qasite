console.log(questions);
var qalist = new Vue({
  el: '#qalist',
  data: {
    questions: questions
  },
  created: function() {
    getQ
  },
  methods: {
    getQ: function(){
      const url = './get_data';
      const options = { method: 'GET' };
      function getQuestionAjax(url, options){
        return fetch(url, options)
            .then( response => response.json() );
      }
      async function getQuestion(url, options){
          const response = await getQuestionAjax(url, options);
          this.questions = response.questions;
          console.log(this.questions);
      }
    }

  }
})
