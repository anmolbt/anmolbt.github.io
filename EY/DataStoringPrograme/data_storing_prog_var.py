import pandas as pd
import json
import numpy as np

df=pd.read_csv("C:/Users/Anmol/Desktop/EY/I am Learning Python/all.csv")

# creating numpy.ndarray of the unique users
unique_users = df.user.unique()
print len(unique_users)

# creating numpy.ndarray of all the unique correspondents
unique_correspondent_ids = df.correspondent_id.unique()
print len(unique_correspondent_ids)

unique_user_nodes =[]
nodes=[]
n=1

# Suppose I just want to work with correspondents having more than 1 unique users.
correspondent_id_nodes=[]

# for i in unique_correspondent_ids:
# 	size=df[df['correspondent_id']==i].shape[0]
# 	if (size!=1):
# 		nodes.append({'id':str(i),'group':30,'size':int(size)})
# 	else:
# 		one_interaction.append({'id':str(i)})

for i in unique_correspondent_ids:
	df4=df[df['correspondent_id']==i]
	size=df4.shape[0]
	suspect=df4.user.unique()
	if(len(suspect)>1):
		nodes.append({'id':str(i),'group':30,'size':int(size)})	
		correspondent_id_nodes.append({'id':str(i),'size':int(size)})


print len(nodes)
for i in unique_users:
	size=df[df['user']==i].shape[0]
	nodes.append({'id':str(i),'group':n,'size':int(size)})
	unique_user_nodes.append({'id':str(i),'size':int(size)})
	n+=1
	
level2d=[]
children=[]

for i in unique_users:
	if(i==7086312446):
		df5=df[df['user']==i]
		unique_user_correspondents=df5.correspondent_id.unique()
		# print len(unique_user_correspondents)
		for unique_correspondent in unique_user_correspondents:
			df6=df[df['correspondent_id']==unique_correspondent]
			suspects=df6.user.unique() #Parent users or child 1 of unique_correspondent
			child1=[]
			for suspect in suspects:
				if(str(suspect)!=str(unique_correspondent)):
					child1.append({'suspect':str(suspect), 'size':2000})
			level2d.append({'user':str(unique_correspondent),'size':int(len(suspects)),'suspects':child1}) 
			# Here user is nothing but unique correspondent
			# ,{'suspects':children}
# 'suspect':children
# ,'suspect':list(suspect}
# print len(unique_user_correspondents)
print level2d

# print nodes
# with open('data_force_layout.json','w') as outf:
# 	json.dump(nodes,outf)
# print 'done'

links=[]

#Extract unique correxpondents of a particular user
for user in unique_users:
	df1= df[df['user']==user]
	unique_user_correspondents=df1.correspondent_id.unique()
	for unique_correspondent in unique_user_correspondents:
		df2=df1[df1['correspondent_id']==unique_correspondent]
		value=df2.shape[0]
		df4=df[df['correspondent_id']==unique_correspondent]
		suspect=df4.user.unique()
		if(len(suspect)>1):
			links.append({'source':str(user),'target':str(unique_correspondent),'value':int(value)})


# print links



graph={'nodes':nodes,'links':links}

unique_users_graph={'unique_users':unique_user_nodes}


correspondent_id_nodes_graph={'correspondent_id_nodes':correspondent_id_nodes}

# 'user':"7086312446",
level2d_graph={'user':"7086312446",'suspects':level2d}

with open('data_force_layout_full.json','w') as outf:
	json.dump(graph,outf)
with open('unique_users.json','w') as outf:
	json.dump(unique_users_graph,outf)
with open('correspondent_nodes.json','w') as outf:
	json.dump(correspondent_id_nodes_graph,outf)
with open('level2d.json','w') as outf:
	json.dump(level2d_graph,outf)

print 'done'






