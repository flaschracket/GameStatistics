using Microsoft.EntityFrameworkCore;
using EF_DataAcessLayer.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EF_DataAcessLayer
{
    public class GameSimulatorDBContext : DbContext
    {
        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {
                optionsBuilder.UseSqlServer(@"Server=.;Database=GameSimulator;Trusted_Connection=True;TrustServerCertificate=True;");
            }

        }
        //entities
        public DbSet<Game> Games { get; set; }
        public DbSet<Player> players { get; set; }

    }
}
