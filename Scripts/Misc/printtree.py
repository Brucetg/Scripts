#-*- coding: utf-8 -*-  
#!/usr/bin/python  
#Filename: BTreeNode.py  
''''' 
Created on 2011-4-11 
@author: boyce 
@contact: boyce.ywr@gmail.com 
@version: 1.0 
'''  
class BTree:  
    ''''' 
    Represent a no in a binary tree. 
    '''  
    def __init__(self, c='/0', l=None, r=None):  
        ''''' 
        Initializes the node's data 
        '''  
        self.e = c  
        self.left = l  
        self.right = r  
def preorderTraverse(bt):  
    ''''' 
    返回前序遍历结果 
    '''  
    if bt:  
        return '%s%s%s' % (bt.e, preorderTraverse(bt.left), preorderTraverse(bt.right))  
    return ''  
def inorderTraverse(bt):  
    ''''' 
    返回中序遍历结果 
    '''  
    if bt:  
        return '%s%s%s' % (inorderTraverse(bt.left), bt.e, inorderTraverse(bt.right))  
    return '';  
def postorderTraverse(bt):  
    ''''' 
    返回后序遍历结果 
    '''  
    if bt:  
        return '%s%s%s' % (postorderTraverse(bt.left), postorderTraverse(bt.right), bt.e)  
    return ''  
def printBTree(bt, depth):  
    ''''' 
    递归打印这棵二叉树，*号表示该节点为NULL 
    '''  
    ''''' 
    if not bt: 
        ch = '*' 
    else: 
        ch = bt.e 
    '''  
    #ch=(lambda x: (x and x.e) or '*')(bt)  
    ch = bt.e if bt else '*'  
    if(depth > 0):  
        print '%s%s%s' % ((depth - 1) * '  ', '--', ch)  
    else:  
        print ch  
    if not bt:  
        return  
    printBTree(bt.left, depth + 1)  
    printBTree(bt.right, depth + 1)  
def buildBTreeFromPreIn(preo, ino):  
    ''''' 
    根据前序和中序遍历结果重构这棵二叉树 
    '''  
    if(preo == '' or ino == ''):  
        return None  
    pos = ino.find(preo[0])  
    if(pos < 0):  
        return None          
    return BTree(preo[0], buildBTreeFromPreIn(preo[1:pos + 1], ino[0:pos]), buildBTreeFromPreIn(preo[pos + 1:], ino[pos + 1:]))  
    #return nd  
def buildBTreeFromInPost(ino, po):  
    ''''' 
    根据中序和后序遍历结果重构这棵二叉树 
    '''  
    if(ino == '' or po == ''):  
        return None  
    pos = ino.find(po[-1])  
    if(pos < 0):  
        return None     
    return BTree(po[-1], buildBTreeFromInPost(ino[0:pos], po[0:pos]), buildBTreeFromInPost(ino[pos + 1:], po[pos:-1]))  
      
if __name__ == '__main__':  
    preo = ''  
    ino = 'RY!heHVaL-goAI{dxj_GpnUw8}kzu*Er:s56fFl2i'  
    po = 'YR!eVa-gLAoxd_j{pw}8zkUnGuIHh:r65f2lFsEi*'  
    bt = buildBTreeFromPreIn(preo, ino)  
    print 'Build from preorder & inorder'  
    print 'Preorder: %s' % (preorderTraverse(bt))  
    print 'Inorder: %s' % (inorderTraverse(bt))  
    print 'Postorder: %s' % (postorderTraverse(bt))  
    print 'The BTree is (* means no such a node):'  
    printBTree(bt, 0)  
    bt = buildBTreeFromInPost(ino, po)  
    print 'Build from inorder & postorder'  
    print 'Preorder: %s' % (preorderTraverse(bt))  
    print 'Inorder: %s' % (inorderTraverse(bt))  
    print 'Postorder: %s' % (postorderTraverse(bt))  
    print 'The BTree is (* means no such a node):'  
    printBTree(bt, 0)  
