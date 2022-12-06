using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GameResources.Game
{
    class Resource
    {
        //bazar, 
        public string Name;
        
        //?resourcetype should be out of object. each resource is one of them
        enum ResourceType
        {
            Board,
            ReservedCard,
            Hardware,
            Function,
        }
        enum Hardware
        {
            CPU
        }
    }
}
