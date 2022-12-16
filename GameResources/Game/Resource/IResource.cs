using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GameResources.Game.Resource
{
    interface IResource
    {
        bool IsPublic();
        ICollection<string> GetType();
        Enum GetStatus();
    }
}
