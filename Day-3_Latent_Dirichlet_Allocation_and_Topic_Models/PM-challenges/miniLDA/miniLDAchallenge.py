#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:01:49 2023

@author: pablo
"""
import os
import random

# settings
pathToDocs = 'documentos'
ldaIterations = #

# hyperparameters
NTOPICS = #
ALPHA = #
BETA  = #


# load documents and words
corpus = []
dictionary = set()
for fname in os.listdir( pathToDocs ):
	document = open(os.path.join(pathToDocs, fname), 'r').read().split(' ')
	corpus.append( document )
	
	words = set( document )
	dictionary = dictionary.union(words)


# random topic assignement per word, per document
topics = range(NTOPICS)
topicOfWordInDocument = []
topicCountInDocument  = []
topicWordCountInCorpus= dict()
for word in dictionary:
	topicWordCountInCorpus[word] = dict( zip(topics, [0]*NTOPICS))
	
for document in corpus:
	topicOfWordInDocument.append([])
	zeroCount = dict( zip(topics, [0]*NTOPICS))
	topicCountInDocument.append(zeroCount)
	
	for word in document:
		randomTopic = random.choice(topics)
		topicOfWordInDocument[-1].append(randomTopic)
		topicCountInDocument[-1][randomTopic] += 1
		topicWordCountInCorpus[word][randomTopic] += 1


# collapsed Gibbs Sampling
print('GIBBS SAMPLING START')
for IT in range(ldaIterations):
	print('ITER: ', IT)
	for di, document in enumerate(corpus):
		for wi, word in enumerate(document):
			# unassign topic of word
			wordTopic = topicOfWordInDocument[di][wi]
			topicCountInDocument[di][wordTopic] -= 1
			topicWordCountInCorpus[word][wordTopic] -= 1
			topicOfWordInDocument[di][wi] = None
			
			#reassign new topic
			
			## EJERCICIO EMPIEZA
			
			## EJERCICIO TERMINA



