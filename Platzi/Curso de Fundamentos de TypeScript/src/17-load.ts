import _ from 'lodash'

const data = [
  {
    username: 'junior',
    role: 'admin'
  },
  {
    username: 'junior1',
    role: 'seller'
  },
  {
    username: 'junior2',
    role: 'seller'
  }
]

const rta2 = _.groupBy(data, (item) => item.role)
console.log(rta2);

const rta = 1 + '1';
