#!/usr/bin/python


class Sentence:
    no_of_words = 2

    def __init__(self):
        self.words = []
        self.is_full = False
        
    def compose(self):
        return " ".join(self.words)
    
    def add_word(self,word):
        if (len(word.split(" ")) == 1):
            if (len(self.words) < self.no_of_words):
                self.words.append(word)
                if (len(self.words) == self.no_of_words):
                    self.is_full = True
                    return 'sentence is full'
                return 'done'
        else:
            return 'multiple'
            
         
class Paragraph:
    no_of_sentences = 2
    
    def __init__(self):
        self.sentences = [] 
        self.is_full = False
    
    def add_word(self,word):
        if len(self.sentences) == 0:
            new_sentence  = Sentence()
            new_sentence.add_word(word)
            self.sentences.append(new_sentence)
            return 'done'
        elif (len(self.sentences) > 0 and len(self.sentences) < self.no_of_sentences):
            current_sentence = self.sentences[len(self.sentences)-1]
            if (current_sentence.is_full):
                new_sentence  = Sentence()
                new_sentence.add_word(word)
                self.sentences.append(new_sentence)
                return 'done'
            elif not current_sentence.is_full:
                current_sentence.add_word(word)
                return 'done'
        elif (len(self.sentences) == self.no_of_sentences):
            current_sentence = self.sentences[len(self.sentences)-1]
            current_sentence.add_word(word)
            if (current_sentence.is_full):
                self.is_full = True
                return 'paragraph is full'
            return 'done'
    
    
class Story:
    no_of_paragraphs = 2
    
    def __init__(self, id = None, created_at =None, updated_at = None, content= None):
        self.paragraphs = []
        self.title = []
        self.id = id
        self.is_full = False
        self.created_at = created_at
        self.updated_at = updated_at
        self.content = content
        if self.content != None:
            self.form_story(content)
        
    def add_word(self,word):
        if (type(word) is not str) or (len(word.split(" ")) != 1):
            return 'error'
        
        if self.is_full == True: 
            return 'story is full'
        
        if len(self.title) < 2:
            self.title.append(word)
            
        elif len(self.title) ==2 :
            if len(self.paragraphs) ==0:
                new_paragraph = Paragraph()
                new_paragraph.add_word(word)
                self.paragraphs.append(new_paragraph)
                return 'done'
            elif (len(self.paragraphs) > 0 and len(self.paragraphs) < self.no_of_paragraphs):
                current_paragraph = self.paragraphs[len(self.paragraphs)-1]
                if (current_paragraph.is_full):
                    new_paragraph  = Paragraph()
                    new_paragraph.add_word(word)
                    self.paragraphs.append(new_paragraph)
                    return 'done'
                elif not current_paragraph.is_full:
                    current_paragraph.add_word(word)
                    return 'done'
            elif (len(self.paragraphs) == self.no_of_paragraphs):
                current_paragraph = self.paragraphs[len(self.paragraphs)-1]
                current_paragraph.add_word(word)
                if (current_paragraph.is_full):
                    self.is_full = True
                    return 'story is full'
                return 'done'
            
    def compose_array(self):
        word_array = []
        for word in self.title:
            word_array.append(word)
        for paragraph in self.paragraphs:
            for sentence in paragraph.sentences:
                for word in sentence.words:
                    word_array.append(word)
        return word_array
    
    def compose_title(self):
        return " ".join(self.title)
            
    
    def form_story(self,array):
        for word in array:
            status = self.add_word(word)
        if status == 'story is full':
            return 'error'
        else:
            return 'done'
        
    def current_sentence(self):
        if len(self.paragraphs) != 0:
            cur_paragraph = self.paragraphs[len(self.paragraphs)-1]
            if cur_paragraph.is_full or len(cur_paragraph.sentences)==0:
                return ""
            else:
                cur_sentence = cur_paragraph.sentences[len(cur_paragraph.sentences)-1]
                if cur_sentence.is_full:
                    return ""
                else: 
                    return cur_sentence.compose()
        else:
            return ""
        
    
                
            
    