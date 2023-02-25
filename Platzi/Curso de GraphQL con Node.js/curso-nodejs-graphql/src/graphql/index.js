const { ApolloServer } = require('apollo-server-express')
const { ApolloServerPluginLandingPageGraphQLPlayground } = require('apollo-server-core')
const { loadFiles } = require('@graphql-tools/load-files')
const resolvers = require('./resolvers')


//  GET = Query
//  POST, PUT, DELETE = Mutations
//  POST = 201
//  POST = CREATE = 201
//  GET = GET DATA
//  PUT = UPDATE
//  DELETE = REMOVE


const useGraphql = async (app) => {
  const server = new ApolloServer({
    typeDefs: await loadFiles('./src/**/*.graphql'),
    resolvers,
    playground: true,
    plugins: [
      ApolloServerPluginLandingPageGraphQLPlayground
    ]
  })
  await server.start()
  server.applyMiddleware({ app })
}

module.exports = useGraphql
