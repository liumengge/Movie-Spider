import pymongo

# 连接数据库
client = pymongo.MongoClient(host='localhost', port=27017)
# client = MongoClient('mongodb://localhost:27017/')

# 指定数据库
db = client.test
# db = client['test']

# 指定集合： collection，类似于关系型数据库中的表
collection = db.students
# collection = db['students']

# 插入数据
# student = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
# result = collection.insert(student)
# print(result)  # 在 MongoDB 中，每条数据其实都有一个 _id 属性来唯一标识。如果没有显式指明该属性，MongoDB 会自动产生一个 ObjectId 类型的 _id 属性。insert() 方法会在执行后返回_id 值

# 同时插入多条数据，只需要以列表形式传递
# student1 = {
#     'id': '20180101',
#     'name': 'Milly',
#     'age': 18,
#     'gender': 'female'
# }
#
# student2 = {
#     'id': '20170202',
#     'name': 'Mike',
#     'age': 21,
#     'gender': 'male'
#
# }
#
# result = collection.insert([student1, student2])
# print(result)

# 在 PyMongo 中，官方已经不推荐使用 insert 方法了，官方推荐使用 insert_one 和 insert_many 方法来分别插入单条记录和多条记录
# student = {
#     'id': '20180102',
#     'name': 'Jo',
#     'age': 21,
#     'gender': 'male'
# }
#
# result = collection.insert_one(student)
# print(result)
# print(result.inserted_id)


# 查询
# 利用 find_one 或 find 方法进行查询，其中 find_one 查询得到的是单个结果，find 则返回一个生成器对象
# result = collection.find_one({'name': 'Mike'})  # 查询 name 为 Mike 的数据，它的返回结果是字典类型
# print(type(result))
# print(result) # 多了 _id 属性，是 MongoDB 在插入过程中自动添加的

# 多条数据查询：find
# results = collection.find({'age': 20})
# print(results) # 返回结果是 Cursor 类型，它相当于一个生成器，我们需要遍历获取的所有结果，其中每个结果都是字典类型。
# for result in results:
#     print(result)

# 如果要查询年龄大于 20 的数据
# results = collection.find({'age': {'$gt': 20}})
# for result in results:
#     print(result)

# 正则匹配查询
# results = collection.find({'name': {'$regex': '^M.*'}})  # 使用 $regex 来指定正则匹配，^M.* 代表以 M 开头的正则表达式。
# for result in results:
#     print(result)

# 计数：count 方法
# count = collection.find().count()
# print(count)
#
# count = collection.find({'age': 20}).count()
# print(count)

# 排序：sort 方法
# results = collection.find().sort('name', pymongo.ASCENDING)  # 调用 pymongo.ASCENDING 指定升序，如果要降序排列，可以传入 pymongo.DESCENDING
# print([result['name'] for result in results])

# 偏移： skip方法
# 某些情况下，我们可能只需要取某几个元素，这时可以利用 skip 方法偏移几个位置，比如偏移 2，就代表忽略前两个元素，得到第 3 个及以后的元素
# results = collection.find().sort('name', pymongo.ASCENDING).skip(2)
# print([result['name'] for result in results])

# limit 方法指定要取的结果个数
# results = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
# print([result['name'] for result in results])
# 值得注意的是，在数据量非常庞大的时候，比如在查询千万、亿级别的数据库时，最好不要使用大的偏移量，
# 因为这样很可能导致内存溢出，此时可以使用类似如下操作来查询：

# from bson.objectid import ObjectId
# collection.find({'_id': {'$gt': ObjectId('593278c815c2602678bb2b8d')}})  # 这时需要记录好上次查询的 _id

# 数据更新：update 方法
condition = {'name': 'Jo'}
student = collection.find_one(condition)
student['age'] = 25
result = collection.update(condition, student)
print(result) # 返回结果是字典形式，ok 代表执行成功，nModified 代表影响的数据条数。
# update 方法其实也是官方不推荐使用的方法。这里也分为 update_one 方法和 update_many 方法，
# 用法更加严格，它们的第 2 个参数需要使用 $ 类型操作符作为字典的键名，具体案例参考拉钩











