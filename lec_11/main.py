import requests;

url = "https://jsonplaceholder.typicode.com/posts";

def getPostsFilteredByTitle():
    response = requests.get(url);
    posts = response.json();
    result = [post for post in posts if len(post['title'].split()) <= 6];
    return result;

def getPostsFilteredByBody():
    response = requests.get(url);
    posts = response.json();
    result = [post for post in posts if len(post['body'].split('\n')) <= 3];
    return result;

def createPost(post):
    response = requests.post(url, post);
    return response;

def updatePost(post):
    response = requests.put(f"{url}/{post['id']}", post);
    return response;

def deletePost(id):
    response = requests.delete(f"{url}/{id}");
    return response;

posts = getPostsFilteredByTitle();
print(f"Count of Posts with Titles with <= 6 words: {len(posts)}");

posts = getPostsFilteredByBody();
print(f"Count of Posts with Bodies with <= 3 rows: {len(posts)}");

post = {
    "title": "New Post",
    "body": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
    "userId": 1
};
result = createPost(post);
print(f"Created Post: {result.json()}");

post = {
    "title": "New Post",
    "body": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
    "userId": 1,
    "id": 40
};
result = updatePost(post);
print(f"Updated Post: {result.json()}");

result = deletePost(17);
if(result.status_code == 200):
    print("Post successfully deleted");
