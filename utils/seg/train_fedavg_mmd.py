import logging
import numpy as np
import torch.nn as nn
import pdb
import torch
import torch.nn.functional as F
from utils.loss_func import Dice_Loss
from utils.loss_mmd import MMD_Loss
import copy
import matplotlib.pyplot as plt

def train(round_idx, client_idx, model, dataloader, optimizer, global_model, args):
    model.train()
    global_model.eval()

    max_epoch = args.max_epoch

    seg_loss = Dice_Loss()
    mmd_loss = MMD_Loss()

    for epoch in range(max_epoch):
        for iters, (_, data) in enumerate(dataloader):
            optimizer.zero_grad()

            image, label = data['image'], data['label']
            image = image.cuda()
            label = label.cuda()

            logit = model(image)[0]
            global_logit = global_model(image)[0]
            
            loss = seg_loss(logit, label)

            logit_avg = logit.mean(dim=1, keepdim=False).reshape(8, -1)
            global_logit_avg = global_logit.mean(dim=1, keepdim=False).reshape(8, -1)
            
            loss_mmd = mmd_loss(logit_avg, global_logit_avg)

            
            loss = loss + loss_mmd 
            
            loss.backward()
            optimizer.step()

    return model
            
