﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GameResources.Game.Resource
{
    public class Board: IResource
    {
        public int Id { get; set; } = 0;
        //public RAM boardRAM =  new();
        public int CPU { get; set; } = 1;
       // public List<IFunction> BoughtFunctions { get; set; }

        public bool IsPublic()
        {
            throw new NotImplementedException();
        }


        public Enum GetStatus()
        {
            throw new NotImplementedException();
        }

        public Enum GetVariation()
        {
            throw new NotImplementedException();
        }
    }
}
