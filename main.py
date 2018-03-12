# Law: git on the blockchain

from hashlib import sha256
from random import randint
from time import time

THROTTLER_RATE = 200
REPUTATION_RATE = 0.000006
REWARD = 0.000010

class Node:
	def __init__(self):
		self.nonce = randint(0, 10**32)
		self.commits = []
		self.repositories = []
		self.timestamp = time()
		self.balance = 0.000000
		self.rep = 0.000002
		self.index = 0

	@property
	def hashid(self):
		h = sha256()
		h.update(bytes(self.nonce + self.timestamp))
		return "user_" + h.hexdigest()

	def registerToChain(self):
		Chain.nodes.append(self)
		self.index = len(Chain.nodes)-1

	def updateCounterpart(self):
		Chain.nodes.pop(self.index)
		Chain.nodes.insert(self.index, self)

	
class Block:
	def __init__(self, parent, commit):
		self.parent = parent
		self.nonce = randint(0, 10**32)
		self.commit = commit
		self.timestamp = time()
		self.mined = False
		self.name = sha256()
		self.name.update(bytes(self.nonce))
		self.name = self.name.hexdigest()


class File:
	def __init__(self, name, body):
		self.name = name
		self.body = body

class Commit:
	def __init__(self, files, repo_id, committer):
		self.files = files
		self.repo_id = repo_id
		self.committer = committer
		self.rep = 0.000000
		self.reward = 0.000000
		self.throttler = 0.000000
		self.name = sha256()
		self.name.update(bytes(randint(0, 2**32)))
		self.name = self.name.hexdigest()

class Repository:
	def __init__(self, creator):
		self.creator = creator
		self.blocks = []
		self.contributors = []
		self.forks = []
		self.current = []
		self.timestamp = time()
		self.name = sha256()
		self.name.update(bytes(randint(0, 2**32)))
		self.name = self.name.hexdigest()

class Chain:
	repos = []
	nodes = []

	def findNode(nodeName):
		x = filter(lambda x: x.name == nodeName, nodes)
		if x:
			return x

	def findRepo(repoId):
		x = filter(lambda x: x.name == repoId, repos)
		if x:
			return x