from TwitterAPI import TwitterAPI, TwitterOAuth, TwitterRequestError, TwitterConnectionError
import json

projects = {
    'BAYC' : {
        'handle': 'BoredApeYC',
        'id': 1381699264011771906
    },
    'CC' : {
        'handle': 'coolcatsnft',
        'id': 1395553778187718657
    },
    'AB' : {
        'handle': 'artblocks_io',
        'id': 1317828734913753090
    },
    'PV' : {
        'handle': 'pixelvault_',
        'id': 1228815654830125060
    }
}

nft_users = {}

o = TwitterOAuth.read_file('./credentials.txt')
api = TwitterAPI(o.consumer_key, o.consumer_secret, o.access_token_key, o.access_token_secret, api_version='2')



def read_users(fname):
    with open(fname) as json_file:
        data = json.load(json_file)
    return data;

def collect_tweets_from_user(user):

    params = {
        'tweet.fields': ['created_at', 'in_reply_to_user_id', 'entities', 'organic_metrics']
    }
    tweets = make_request(f'users/:{user.id}/tweets', params)
    for tweet in tweets:

        ## get date
        date = tweet.created_at

        ## does it mention other users in our data set?

        ## is it a reply to another tweet from someone in our data set?
        if (tweet.in_reply_to_user_id):
            is_in_base = tweet.in_reply_to_user_id in nft_users
            

        ## is it a retweet from another user in our data set


        ## get organic metrics (impresssions, profile clicks, likes, retweets, replies, quote tweets)
        organic_metrics = tweet.entities.organic_metrics


def retrieve_users(): 
    for proj, info in projects.items():
            
        proj_id = info['id']
        print(f'project: {proj}')
        following = make_request(f'users/:{proj_id}/following')

        followingList = []
        for f in following:
            followingList.append(f)
        #     if (f['id'] not in nft_users):
        #         nft_users[f['id']] = {
        #             'name': f['name'],
        #             'handle': f['username']
        #         }

        followers = make_request(f'users/:{proj_id}/followers')
        followerList = []
        for f in followers:
            followerList.append(f)
        #     if (f['id'] not in nft_users):
        #         nft_users[f['id']] = {
        #             'name': f['name'],
        #             'handle': f['username']
        #         }
        
        print(f'followers: {len(followerList)}')
        print(f'following: {len(followingList)}')
        # file = open("users1.json", "w")
        # json.dump(nft_users, file)
        # file.close()

def make_request(url, params={}):
    try:
        if params:
            return api.request(url, params)
        else:
            return api.request(url)

    except TwitterRequestError as e:
        print(e.status_code)
        for msg in iter(e):
            print(msg)

    except TwitterConnectionError as e:
        print(e)

    except Exception as e:
        print(e)

retrieve_users()