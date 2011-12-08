from nltk import pos_tag, word_tokenize

class Parser:
	
	def identify(self, msg):
		return pos_tag(word_tokenize(msg))
	
	def get_nouns(self, msg):
		data = self.identify(msg)
		nouns = []
		for w in data:
			if w[1].startswith('NN'):
				nouns.append(w[0])
		return nouns
		
	def get_proper_nouns(self, msg):
		data = self.identify(msg)
		propers = []
		for w in data:
			if w[1].startswith('NNP'):
				propers.append(w[0])
		return propers
				
	def get_verbs(self, msg):
		data = self.identify(msg)
		verbs = []
		for w in data:
			if w[1].startswith('V'):
				verbs.append(w[0])
		return verbs

	def get_adjectives(self, msg):
		data = self.identify(msg)
		adjs = []
		for w in data:
			if w[1].startswith('JJ'):
				adjs.append(w[0])
		return adjs
	
	def get_tags(self, msg):
		tags = []
		for w in msg.split():
			if w.startswith('@'):
				tags.append(w);
		return tags
		
	def get_hashtags(self, msg):
		hashs = []
		for w in msg.split():
			if w.startswith('#'):
				hashs.append(w);
		return hashs
		
	def get_links(self, msg):
		links = []
		for w in msg.split():
			if w.startswith('www') or w.startswith('http://'):
				links.append(w);
		return links
		
	def extract(self, msg):
		propers = self.get_proper_nouns(msg)
		nouns = self.get_nouns(msg)
		verbs = self.get_verbs(msg)
		adjs = self.get_adjectives(msg)
		links = self.get_links(msg)
		tags = self.get_tags(msg)
		hashtags = self.get_hashtags(msg)
		return (propers, nouns, verbs, adjs, links, tags, hashtags)
		
