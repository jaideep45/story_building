#!/usr/bin/python
from docutils.nodes import paragraph
from __builtin__ import str


class Sentence:
    no_of_words = 15

    def __init__(self):
        self.words = []
        
    def compose(self):
        full_sentence = ""
        for word in self.words:
            full_sentence = full_sentence + word
        return full_sentence
    
    def add_word(self,word):
        if (len(word.split(" ")) == 1):
            if (len(self.words) < self.no_of_words):
                self.words.append(word)
                return 'done'
            elif (len(self.words) == self.no_of_words):
                return 'sentence is full'
        else:
            return 'multiple'
            
         
class Paragraph:
    no_of_sentences = 10
    
    def __init__(self):
        self.sentences = [] 
    
    def add_word(self,word):
        if len(self.sentences) == 0:
            new_sentence  = Sentence()
            new_sentence.add_word(word)
            self.sentences.append(new_sentence)
            return 'done'
        elif (len(self.sentences) > 1 & len(self.sentences) <= self.no_of_sentences):
            current_sentence = self.sentences[len(self.sentences)-1]
            if (current_sentence.add_word(word) == 'sentence is full'):
                new_sentence  = Sentence()
                new_sentence.add_word(word)
                self.sentences.append(new_sentence)
                return 'done'
            elif (current_sentence.add_word(word) == 'done'):
                return 'done'
        elif (len(self.sentences) == self.no_of_sentences):
            if (current_sentence.add_word(word) == 'sentence is full'):
                return 'paragraph is full'
            elif (current_sentence.add_word(word) == 'done'):
                return 'done'
    
    
class Story:
    no_of_paragraphs = 7
    
    def __init__(self):
        self.paragraphs = []
        
    def add_word(self,word):
        if type(word) is str & len(word.split(" ")) == 1:
            if len(self.paragraphs) ==0:
                new_paragraph = Paragraph()
                new_paragraph.add_word(word)
                self.paragraphs.append(new_paragraph)
                return 'done'
            elif (len(self.paragraphs) > 1 & len(self.paragraphs) <= self.no_of_paragraphs):
                current_paragraph = self.paragraphs[len(self.paragraphs)-1]
                if (current_paragraph.add_word(word) == 'paragraph is full'):
                    new_paragraph  = Paragraph()
                    new_paragraph.add_word(word)
                    self.paragraphs.append(new_paragraph)
                    return 'done'
                elif (current_paragraph.add_word(word) == 'done'):
                    return 'done'
            elif (len(self.paragraphs) == self.no_of_paragraphs):
                if (current_paragraph.add_word(word) == 'paragraph is full'):
                    return 'story is full'
                elif (current_paragraph.add_word(word) == 'done'):
                    return 'done'
        else:
            return 'multiple string'
            
    def compose_array(self):
        word_array = []
        for paragraph in self.paragraphs:
            for sentence in paragraph.sentences:
                for word in sentence.words:
                    word_array.append(word)
        return word_array
    
    def form_story(self,array):
        for word in array:
            status = self.add_word(word)
            if status == 'story is full':
                return 'error'
            else:
                return 'done'
    
#     def update(self,id):
                
            
    