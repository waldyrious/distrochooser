import Vapi from 'vuex-rest-api'
import Vuex from 'vuex'

const indexStore = new Vapi({
  baseURL: 'MISSING',
  state: {
    categories: [
      {
        id: 'cat1',
        title: 'category'
      },
      {
        id: 'cat2',
        title: 'category2'
      }
    ],
    category: {
      id: 'cat1',
      title: 'category'
    },
    question: {
      id: 'somestupidid',
      title: 'This is a test question',
      isMultipleChoice: true,
      answers: [
        {
          id: 'jfaklsfjxla1',
          text: 'foo',
          isImportant: false,
          isAnswered: false
        },
        {
          id: 'jfaklsfjxla3',
          text: 'bar',
          isImportant: false,
          isAnswered: false
        },
        {
          id: 'jfaklsfjxla2',
          text: 'barz',
          isImportant: false,
          isAnswered: false
        }
      ]
    }
  }
})
  .get({
    action: 'getCategories',
    property: 'categories',
    path: () => `/categories`
  })
  .getStore()

indexStore.actions.answerQuestion = (store, payload) => {
  // TODO: push answer to server
  // TODO: Read result
  var answer = payload.selectedAnswer
  store.state.question.answers.forEach(a => {
    a.isAnswered =
      a.id === answer.id
        ? !a.isAnswered
        : !store.state.question.isMultipleChoice
          ? false
          : a.isAnswered
  })
}

indexStore.actions.selectCategory = (store, payload) => {
  var category = payload.selectedCategory
  store.state.category = category
  //TODO: trigger question change
  //TODO: load the question
}

const createStore = () => {
  return new Vuex.Store(indexStore)
}

export default createStore
