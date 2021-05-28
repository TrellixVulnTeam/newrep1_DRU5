import elasticsearch


class search(elasticsearch.Elasticsearch):
    def twitter_trends(self, index, channel, size):
        result = []
        try:
            object = self.es.search(
                index=index,
                body={
                    "query": {

                        "must": {
                            "channel": channel

                        },

                    },
                    "size": size,
                    "from": 0

                }

            )
            for i in object['hits']['hits']:
                result.append(i['_source'])
            return result
        except Exception as error:
            print(error)

    def youtube_trends(self, index, country, size):
        real_result = []
        try:
            result = self.es.search(
                index=index,
                body={
                    'query': {
                        'bool': {
                            'must': [
                                {
                                    'match': {
                                        'youtube.country': country

                                    }
                                },

                            ]

                        }

                    },
                    'size': size,
                    'from': 0,

                },

            )
            for i in result['hits']['hits']:
                real_result.append(i['_source'])
        except  Exception as error:
            print(error)

    def disp_twitter_trends(self, index, gte, lte):
        result = []
        try:
            res = self.es.search(
                index=index,
                body={
                    'query': {
                        'range': {
                            'created_on': {
                                'gte': gte * 100,
                                'lte': lte * 100

                            }

                        }

                    },
                    'size': 20,
                    'from': 0
                }

            )
            for i in result['hits']['hits']:
                res.append(i['_source'])


        except Exception as error:
            print(error)

    def google_trends_elasticsearch(self, index):
        try:
            real_result = []
            result = self.es.search(
                index=index,
                body={
                    'query': {
                        'match_all': {

                        }
                    }, 'size': 20,
                    'from': 0,
                    'sort': {
                        'created_on': {
                            'order': 'desc'
                        }

                    }
                }
            )

            for i in result['hits']['hits']:
                return real_result.append(i['_source'])
        except Exception as error:
            print(error)
