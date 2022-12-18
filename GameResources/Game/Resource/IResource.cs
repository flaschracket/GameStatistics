﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GameResources.Game.Resource
{
    public interface IResource
    {
        bool IsPublic();
        Enum GetVariation();
        Enum GetStatus();
    }
}
