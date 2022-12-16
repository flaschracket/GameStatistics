using GameResources.Game.Resource;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GameResources.Game.Resource
{
    public class Resource: IResource
    {
        //bazar, 
        public string Name;

        public Enum GetStatus()
        {
            throw new NotImplementedException();
        }

        public bool IsPublic()
        {
            throw new NotImplementedException();
        }

        ICollection<string> IResource.GetType()
        {
            throw new NotImplementedException();
        }

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
