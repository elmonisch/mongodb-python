import pymongo
import timeit

conn_str = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn_str)

db = client.the_small_bookstore

if db.books.count() == 0:
    print("Inserting data")
    # insert some data...
    r = db.books.insert_one({'title': 'The first book', 'isbn': '7263512736'})
    print(r, type(r))
    r = db.books.insert_one({'title': 'The second book', 'isbn': '237648723'})
    print(r.inserted_id)
else:
    print("books already inserted, skipping..")

# test query
# print(f'There are {db.books.count()} books')
# print(f'First book : {db.books.find_one()}')
# print('Book by ISBN : {}'.format(db.books.find_one({'isbn': '7263512736'})))

tic = timeit.default_timer()
book = db.books.find_one({'isbn': '7263512736'})
book['favourited_by'] = []
book['favourited_by'].append(100)
db.books.update({'_id': book.get('_id')}, book)
book = db.books.find_one({'isbn': '7263512736'})
print('time : ', timeit.default_timer() - tic)
print(book)

tic = timeit.default_timer()
db.books.update({'isbn': '7263512736'}, {'$push': {'favourited_by': 1203}})
book = db.books.find_one({'isbn': '7263512736'})
print('time : ', timeit.default_timer() - tic)
print(book)