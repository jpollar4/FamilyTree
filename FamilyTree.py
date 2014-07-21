import random

class Person:
	def __init__(self, name, parents, children, spouse, generation):
		self.name = name
		self.parents = parents
		self.children = children
		self.spouse = spouse
		self.generation = generation


def findUnmarriedPersonMyAge(personLookingForLove):
	nMyAge = personLookingForLove.generation;

	#get farthestBack on one side
	rootNode = None;
	if(personLookingForLove.parents.__len__() > 0):
		rootNode = personLookingForLove.parents[0]
	else:
		return None
	oldRoot = None;
	while(True):
		oldRoot = rootNode
		if(rootNode.parents.__len__() > 0):
			rootNode= rootNode.parents[0]
		else:
			break;
	rootNode = oldRoot;
	candidate = None;
	#tranverse from root
	for i in rootNode.children:		
		if personLookingForLove in i.children:
			print "incest! eww"
			continue;
		if(i.generation < nMyAge):
			candidate = findUnmarriedPersonMyAge_recurse(personLookingForLove, i)
		if candidate!=None:
			return candidate

	return None

def findUnmarriedPersonMyAge_recurse(personLookingForLove, node):
	nMyAge = personLookingForLove.generation;

	#tranverse from root
	for i in node.children:
		if personLookingForLove in i.children:
			print "incest! eww"
			break;
		if(i.generation < nMyAge):
			findUnmarriedPersonMyAge_recurse(personLookingForLove, i);
		if(i.generation == nMyAge):
			if i.spouse == None:
				return i
		else:
			return None;
	return None;

def addChild(name, parents, names):
	nGeneration = 0;
	if(parents.__len__() > 0):
		nGeneration = parents[0].generation + 1;
	if(nGeneration >= 10):
		return None
	newChild = Person(name,parents,[],None,nGeneration);
	for parent in parents:
		parent.children.append(newChild)

	#will I marry?
	#spouse = findUnmarriedPersonMyAge(newChild);
	#if(spouse == None):	
	spouse = Person(random.choice(names),[],[],newChild,nGeneration);
	spouse.spouse = newChild;
	newChild.spouse = spouse
	#have children?
	for i in range(0,2):
		myChild = addChild(random.choice(names), [newChild, spouse],names)

	return newChild

def printFamily(rootNode):
	strIndent = ''
	for i in range(0,rootNode.generation):
		strIndent += '    |'


	print strIndent+"My Name:" + str(rootNode.name)
	#print strIndent+"generation: " + str(rootNode.generation)	
	print strIndent+"Spouse:" + str(rootNode.spouse.name)
	
	for i in rootNode.children:
		print strIndent+"Child of " + str(rootNode.name)+" is " + str(i.name)
		printFamily(i);
	
		



names = []
nameFile = open('names.txt');

for i in nameFile:
	names.append(i.rstrip())

child = addChild(random.choice(names),[],names)

printFamily(child)
